"""Functions related to detecting the updated entities

This function mostly runs SQL sentences to put:

- FlagUpdated = 1
- LastUpdate = SYSDATE

This happens for the different types of Entitites (PROD,
PAGE, IMPR, CONT, SUBJ y the pseudo entity _DSP).

It also tries to figure out if some files changed (ex:
biographies, pictures, etc) and place marks on these
entities too.

Another function (the "delta" command) then can take these
marked entities and generate the regeneration jobs.

"""

import ecommerce.config
import ecommerce.db
from   ecommerce.queue import *

from globals import *


#########################################################
#########################################################
#
# COMMAND - UPDATES
#
def cmd_updates(arguments):
    """Update the Stage0_* tables
    
    NOTE: this does not go as a job into the queue because the
          Stage0_* tables are used to actualy generate jobs in
          the queue, if the table is not up-to-date when jobs
          are being generated...
    """

    #
    # ***IMPORTANT***
    #
    # these queries are taken from repository catalog,
    # file bulk/stage0/Stage0_DeltaControl_update.sql
    #
    # Each entity is updated according to the following plan:
    #
    # 1. the control table is updated with the current
    #    time (field NewUpdateDate)
    # 2. missing entries are added (for new records)
    # 3. entities that have updates in the
    #    [ LastUpdateDate, NewUpdateDate) are marked as
    #    changed
    # 4. external resources (images, txt files, etc) are checked
    #    for changed (done in Python)
    # 5. the control table is marked with the new last date
    #    (field LastUpdateDate = NewUpdateDate)
    #
    # ****IMPORTANT****
    #
    # the sequence of queries was altered (from the mentioned
    # sql file) in order to get an update method that requires
    # **NO** synchronization and can recover properly without
    # any manual intervention.
    #
    # The change is that each entity propagates the "updated"
    # flag to the corresponding dependent entities (ex: CONT
    # propagates to PROD, IMPR propagates to PROD, PROD
    # propagates to PAGE, etc).
    #
    # Done this way, when we are taking the records with
    # FlagUpdated = 1 to generate the queue commands, we can
    # select the Stage0_Delta records with FlagUpdated = 1 
    # **AND** LastUpdate **LESS THAN OR EQUAL** to
    # Stage0_DeltaControl.LastUpdated.
    #
    # This little change makes it possible for the algorithm
    # to work and self recover from failures, even if the deltas
    # keep being calculated but not being processed!!!
    #
    queries = [
        # ---------------------------------------------
        # ---------------------------------------------
        # --
        # -- entity CONT
        # --
        # ---------------------------------------------
        # ---------------------------------------------
        {
            "entity"    : "CONT",
            "desc"      : "Set new max update date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         NewUpdateDate       = SYSDATE
                    WHERE       EntityType = 'CONT'
            """
        },
        {
            "entity"    : "CONT",
            "desc"      : "Create Delta entries for new records",
            "query"     : """
                INSERT INTO Stage0_Delta(EntityType, EntityId, FlagUpdated, FlagMain,
                                        FlagPrice, FlagComments, FlagRelated, LastUpdate)
                SELECT          'CONT'                  AS EntityType,
                                Id_Autor                AS EntityId,
                                1                       AS FlagUpdated,
                                0                       AS FlagMain,
                                0                       AS FlagPrice,
                                0                       AS FlagComments,
                                0                       AS FlagRelated,
                                (SELECT     LastUpdateDate
                                    FROM    Stage0_DeltaControl
                                    WHERE   EntityType = 'CONT')
                                                        AS LastUpdate
                    FROM        Autores
                    WHERE       Id_Autor NOT IN (
                                    SELECT      EntityId
                                        FROM    Stage0_Delta
                                        WHERE   EntityType = 'CONT'
                                )
                    ORDER BY    Id_Autor
            """
        },
        {
            "entity"    : "CONT",
            "desc"      : "Mark updated records",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'CONT')
                    WHERE       EntityType = 'CONT' AND
                                EntityId IN (
                                    --
                                    -- Autores (NO INDEX ON F_Modi)
                                    --
                                    SELECT          A.Id_Autor
                                        FROM        Autores A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'CONT') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'CONT')
                                    UNION
                                    --
                                    -- Articulos_Autores (NO INDEX ON F_Modi)
                                    --
                                    SELECT          A.Id_Autor
                                        FROM        Articulos_Autores A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'CONT') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'CONT')
                                )
            """
        },
        #
        # TODO - check biographies
        #
        {
            "entity"    : "CONT",
            "desc"      : "Mark dependents - PROD",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'PROD')
                    WHERE       EntityType = 'PROD' AND
                                EntityId IN (
                                    --
                                    -- all PRODs with a CONT that changed
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos_Autores A
                                        WHERE       A.Id_Autor IN (
                                            SELECT          S0.EntityId
                                                FROM        Stage0_Delta S0
                                                WHERE       S0.EntityType = 'CONT' AND
                                                            S0.FlagUpdated = 1
                                            )
                                )
            """
        },
        {
            "entity"    : "CONT",
            "desc"      : "Set new last processed date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         LastUpdateDate      = NewUpdateDate
                    WHERE       EntityType = 'CONT'
            """
        },
        # ---------------------------------------------
        # ---------------------------------------------
        # --
        # -- entity IMPR
        # --
        # ---------------------------------------------
        # ---------------------------------------------
        {
            "entity"    : "IMPR",
            "desc"      : "Set new max update date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         NewUpdateDate       = SYSDATE
                    WHERE       EntityType = 'IMPR'
            """
        },
        {
            "entity"    : "IMPR",
            "desc"      : "Create Delta entries for new records",
            "query"     : """
                INSERT INTO Stage0_Delta(EntityType, EntityId, FlagUpdated, FlagMain,
                                        FlagPrice, FlagComments, FlagRelated, LastUpdate)
                SELECT          'IMPR'                  AS EntityType,
                                Id_Editor               AS EntityId,
                                1                       AS FlagUpdated,
                                0                       AS FlagMain,
                                0                       AS FlagPrice,
                                0                       AS FlagComments,
                                0                       AS FlagRelated,
                                (SELECT     LastUpdateDate
                                    FROM    Stage0_DeltaControl
                                    WHERE   EntityType = 'IMPR')
                                                        AS LastUpdate
                    FROM        Editores
                    WHERE       Id_Editor NOT IN (
                                    SELECT      EntityId
                                        FROM    Stage0_Delta
                                        WHERE   EntityType = 'IMPR'
                                )
                    ORDER BY    Id_Editor
            """
        },
        {
            "entity"    : "IMPR",
            "desc"      : "Mark updated records",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'IMPR')
                    WHERE       EntityType = 'IMPR' AND
                                EntityId IN (
                                    --
                                    -- Editores
                                    --
                                    SELECT          E.Id_Editor
                                        FROM        Editores E
                                        WHERE       E.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'IMPR') AND
                                                    E.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'IMPR')
                                )
            """
        },
        {
            "entity"    : "IMPR",
            "desc"      : "Mark dependents - PROD",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'PROD')
                    WHERE       EntityType = 'PROD' AND
                                EntityId IN (
                                    --
                                    -- all PRODs with a IMPR that changed
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos A
                                        WHERE       A.Id_Editor IN (
                                            SELECT          S0.EntityId
                                                FROM        Stage0_Delta S0
                                                WHERE       S0.EntityType = 'IMPR' AND
                                                            S0.FlagUpdated = 1
                                            )
                                )
            """
        },
        {
            "entity"    : "IMPR",
            "desc"      : "Set new last processed date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         LastUpdateDate      = NewUpdateDate
                    WHERE       EntityType = 'IMPR'
            """
        },
        # ---------------------------------------------
        # ---------------------------------------------
        # --
        # -- entity SUBJ
        # --
        # ---------------------------------------------
        # ---------------------------------------------
        {
            "entity"    : "SUBJ",
            "desc"      : "Set new max update date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         NewUpdateDate       = SYSDATE
                    WHERE       EntityType = 'SUBJ'
            """
        },
        {
            "entity"    : "SUBJ",
            "desc"      : "Create Subject entries for new records",
            "query"     : """
                INSERT INTO Stage0_Subjects(SubjectId, Categoria_Seccion, Categoria_Grupo,
                                            Categoria_Familia, Categoria_Subfamilia, Subtype)
                SELECT              ROWNUM + (SELECT MAX(S0.SubjectId) FROM Stage0_Subjects S0),
                                    Categoria_Seccion,
                                    Categoria_Grupo,
                                    Categoria_Familia,
                                    Categoria_Subfamilia,
                                    Subtype
                    FROM            (
                        SELECT              S.Categoria_Seccion,
                                            S.Categoria_Grupo,
                                            S.Categoria_Familia,
                                            S.Categoria_Subfamilia,
                                            S.Subtype
                            FROM            (
                                SELECT          Categoria_Seccion               AS Categoria_Seccion,
                                                -1                              AS Categoria_Grupo,
                                                -1                              AS Categoria_Familia,
                                                -1                              AS Categoria_Subfamilia,
                                                'Seccion'                       AS Subtype
                                    FROM        Categ_Secciones
                                    WHERE       Categoria_Seccion IN (1, 3, 4, 5)
                                UNION
                                SELECT          Categoria_Seccion               AS Categoria_Seccion,
                                                Categoria_Grupo                 AS Categoria_Grupo,
                                                -1                              AS Categoria_Familia,
                                                -1                              AS Categoria_Subfamilia,
                                                'Grupo'                         AS Subtype
                                    FROM        Categ_Grupos
                                    WHERE       Categoria_Seccion IN (1, 3, 4, 5)
                                UNION
                                SELECT          Categoria_Seccion               AS Categoria_Seccion,
                                                Categoria_Grupo                 AS Categoria_Grupo,
                                                Categoria_Familia               AS Categoria_Familia,
                                                -1                              AS Categoria_Subfamilia,
                                                'Familia'                       AS Subtype
                                    FROM        Categ_Familias
                                    WHERE       Categoria_Seccion IN (1, 3, 4, 5)
                                UNION
                                SELECT          Categoria_Seccion               AS Categoria_Seccion,
                                                Categoria_Grupo                 AS Categoria_Grupo,
                                                Categoria_Familia               AS Categoria_Familia,
                                                Categoria_Subfamilia            AS Categoria_Subfamilia,
                                                'Subfamilia'                    AS Subtype
                                    FROM        Categ_Subfamilias
                                    WHERE       Categoria_Seccion IN (1, 3, 4, 5)
                                ORDER BY        Categoria_Seccion, Categoria_Grupo, Categoria_Familia, Categoria_Subfamilia
                            ) S
                            WHERE   (S.Categoria_Seccion, S.Categoria_Grupo, S.Categoria_Familia,
                                     S.Categoria_Subfamilia, S.Subtype) NOT IN (
                                             SELECT     SS.Categoria_Seccion,
                                                        SS.Categoria_Grupo,
                                                        SS.Categoria_Familia,
                                                        SS.Categoria_Subfamilia,
                                                        SS.Subtype
                                                  FROM  Stage0_Subjects SS
                                    )
                            ORDER BY            S.Categoria_Seccion, S.Categoria_Grupo, S.Categoria_Familia,
                                                S.Categoria_Subfamilia
                    )
            """
        },

        {
            "entity"    : "SUBJ",
            "desc"      : "Create Delta entries for new records",
            "query"     : """

                INSERT INTO Stage0_Delta(EntityType, EntityId, FlagUpdated, FlagMain,
                                        FlagPrice, FlagComments, FlagRelated, LastUpdate)
                SELECT          'SUBJ'                  AS EntityType,
                                SubjectId               AS EntityId,
                                1                       AS FlagUpdated,
                                0                       AS FlagMain,
                                0                       AS FlagPrice,
                                0                       AS FlagComments,
                                0                       AS FlagRelated,
                                (SELECT     LastUpdateDate
                                    FROM    Stage0_DeltaControl
                                    WHERE   EntityType = 'SUBJ')
                                                        AS LastUpdate
                    FROM        Stage0_Subjects
                    WHERE       SubjectId NOT IN (
                                    SELECT      EntityId
                                        FROM    Stage0_Delta
                                )
                    ORDER BY    SubjectId
            """
        },
        {
            "entity"    : "SUBJ",
            "desc"      : "Mark updated records",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'SUBJ')
                    WHERE       EntityType = 'SUBJ' AND
                                EntityId IN (
                                    --
                                    -- Categ_Secciones (NO INDEX ON F_Modi)
                                    --
                                    SELECT          S.SubjectId
                                        FROM        Categ_Secciones C
                                        INNER JOIN  Stage0_Subjects S
                                            ON      C.Categoria_Seccion     = S.Categoria_Seccion   AND
                                                    S.Categoria_Grupo       = -1                    AND
                                                    S.Categoria_Familia     = -1                    AND
                                                    S.Categoria_Subfamilia  = -1
                                        WHERE       C.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'SUBJ') AND
                                                    C.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'SUBJ')
                                    UNION
                                    --
                                    -- Categ_Grupos (NO INDEX ON F_Modi)
                                    --
                                    SELECT          S.SubjectId
                                        FROM        Categ_Grupos C
                                        INNER JOIN  Stage0_Subjects S
                                            ON      C.Categoria_Seccion     = S.Categoria_Seccion   AND
                                                    C.Categoria_Grupo       = S.Categoria_Grupo     AND
                                                    S.Categoria_Familia     = -1                    AND
                                                    S.Categoria_Subfamilia  = -1
                                        WHERE       C.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'SUBJ') AND
                                                    C.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'SUBJ')
                                    UNION
                                    --
                                    -- Categ_Familias (NO INDEX ON F_Modi)
                                    --
                                    SELECT          S.SubjectId
                                        FROM        Categ_Familias C
                                        INNER JOIN  Stage0_Subjects S
                                            ON      C.Categoria_Seccion     = S.Categoria_Seccion   AND
                                                    C.Categoria_Grupo       = S.Categoria_Grupo     AND
                                                    C.Categoria_Familia     = S.Categoria_Familia   AND
                                                    S.Categoria_Subfamilia  = -1
                                        WHERE       C.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'SUBJ') AND
                                                    C.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'SUBJ')
                                    UNION
                                    --
                                    -- Categ_Subfamilias (NO INDEX ON F_Modi)
                                    --
                                    SELECT          S.SubjectId
                                        FROM        Categ_Subfamilias C
                                        INNER JOIN  Stage0_Subjects S
                                            ON      C.Categoria_Seccion     = S.Categoria_Seccion   AND
                                                    C.Categoria_Grupo       = S.Categoria_Grupo     AND
                                                    C.Categoria_Familia     = S.Categoria_Familia   AND
                                                    C.Categoria_Subfamilia  = S.Categoria_Subfamilia
                                        WHERE       C.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'SUBJ') AND
                                                    C.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'SUBJ')
                                )
            """
        },
        {
            "entity"    : "SUBJ",
            "desc"      : "Mark dependents - PAGE",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'PAGE')
                    WHERE       EntityType = 'PAGE' AND
                                EntityId = 1 AND
                                EXISTS (SELECT      1
                                            FROM    Stage0_Delta D
                                            WHERE   D.EntityType = 'SUBJ' AND
                                                    D.FlagUpdated = 1)
            """
        },
        {
            "entity"    : "SUBJ",
            "desc"      : "Mark dependents - PROD",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'PROD')
                    WHERE       EntityType = 'PROD' AND
                                EntityId IN (
                                    --
                                    -- all PRODs with a SUBJ that changed
                                    --
                                    -- NOTE: this is opened in 4 subqueries
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Stage0_Subjects S
                                        INNER JOIN  Articulos A
                                            ON      S.Categoria_Seccion     = A.Categoria_Seccion
                                        WHERE       S.SubjectId IN (
                                                        SELECT          S0.EntityId
                                                            FROM        Stage0_Delta S0
                                                            WHERE       S0.EntityType = 'SUBJ'  AND
                                                                        S0.FlagUpdated = 1)     AND
                                                    S.Subtype = 'Seccion'
                                    UNION
                                    SELECT          A.Id_Articulo
                                        FROM        Stage0_Subjects S
                                        INNER JOIN  Articulos A
                                            ON      S.Categoria_Seccion     = A.Categoria_Seccion AND
                                                    S.Categoria_Grupo       = A.Categoria_Grupo
                                        WHERE       S.SubjectId IN (
                                                        SELECT          S0.EntityId
                                                            FROM        Stage0_Delta S0
                                                            WHERE       S0.EntityType = 'SUBJ'  AND
                                                                        S0.FlagUpdated = 1)     AND
                                                    S.Subtype = 'Grupo'
                                    UNION
                                    SELECT          A.Id_Articulo
                                        FROM        Stage0_Subjects S
                                        INNER JOIN  Articulos A
                                            ON      S.Categoria_Seccion     = A.Categoria_Seccion   AND
                                                    S.Categoria_Grupo       = A.Categoria_Grupo     AND
                                                    S.Categoria_Familia     = A.Categoria_Familia
                                        WHERE       S.SubjectId IN (
                                                        SELECT          S0.EntityId
                                                            FROM        Stage0_Delta S0
                                                            WHERE       S0.EntityType = 'SUBJ' AND
                                                                        S0.FlagUpdated = 1) AND
                                                    S.Subtype = 'Familia'
                                    UNION
                                    SELECT          A.Id_Articulo
                                        FROM        Stage0_Subjects S
                                        INNER JOIN  Articulos A
                                            ON      S.Categoria_Seccion     = A.Categoria_Seccion   AND
                                                    S.Categoria_Grupo       = A.Categoria_Grupo     AND
                                                    S.Categoria_Familia     = A.Categoria_Familia   AND
                                                    S.Categoria_Subfamilia  = A.Categoria_Subfamilia
                                        WHERE       S.SubjectId IN (
                                                        SELECT          S0.EntityId
                                                            FROM        Stage0_Delta S0
                                                            WHERE       S0.EntityType = 'SUBJ' AND
                                                                        S0.FlagUpdated = 1) AND
                                                    S.Subtype = 'Subfamilia'
                                )
            """
        },
        {
            "entity"    : "SUBJ",
            "desc"      : "Set new last processed date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         LastUpdateDate      = NewUpdateDate
                    WHERE       EntityType = 'SUBJ'
            """
        },
        # ---------------------------------------------
        # ---------------------------------------------
        # --
        # -- entity _DSP
        # --
        # ---------------------------------------------
        # ---------------------------------------------
        {
            "entity"    : "_DSP",
            "desc"      : "Set new max update date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         NewUpdateDate       = SYSDATE
                    WHERE       EntityType = '_DSP'
            """
        },
        {
            "entity"    : "_DSP",
            "desc"      : "Create Delta entries for new records",
            "query"     : """
                INSERT INTO Stage0_Delta(EntityType, EntityId, FlagUpdated, FlagMain,
                                        FlagPrice, FlagComments, FlagRelated, LastUpdate)
                SELECT          '_DSP'                  AS EntityType,
                                Id_Disponibilidad       AS EntityId,
                                1                       AS FlagUpdated,
                                0                       AS FlagMain,
                                0                       AS FlagPrice,
                                0                       AS FlagComments,
                                0                       AS FlagRelated,
                                (SELECT     LastUpdateDate
                                    FROM    Stage0_DeltaControl
                                    WHERE   EntityType = '_DSP')
                                                        AS LastUpdate
                    FROM        Disponibilidades
                    WHERE       Id_Esquema = 'PROD' AND
                                Id_Disponibilidad NOT IN (
                                    SELECT      EntityId
                                        FROM    Stage0_Delta
                                        WHERE   EntityType = '_DSP'
                                )
                    ORDER BY    Id_Disponibilidad
            """
        },
        {
            "entity"    : "_DSP",
            "desc"      : "Mark updated records",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = '_DSP')
                    WHERE       EntityType = '_DSP' AND
                                EntityId IN (
                                    SELECT          D.Id_Disponibilidad
                                        FROM        Disponibilidades D
                                        WHERE       D.Id_Esquema = 'PROD' AND
                                                    D.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = '_DSP') AND
                                                    D.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = '_DSP')
                                )
            """
        },
        {
            "entity"    : "_DSP",
            "desc"      : "Mark dependents - PROD",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'PROD')
                    WHERE       EntityType = 'PROD' AND
                                EntityId IN (
                                    --
                                    -- all PRODs with a _DSP that changed
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos A
                                        WHERE       A.Id_Disponibilidad IN (
                                            SELECT          S0.EntityId
                                                FROM        Stage0_Delta S0
                                                WHERE       S0.EntityType = '_DSP' AND
                                                            S0.FlagUpdated = 1
                                            )
                                )
            """
        },
        {
            "entity"    : "_DSP",
            "desc"      : "Set new last processed date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         LastUpdateDate      = NewUpdateDate
                    WHERE       EntityType = '_DSP'
            """
        },
        # ---------------------------------------------
        # ---------------------------------------------
        # --
        # -- entity PROD
        # --
        # ---------------------------------------------
        # ---------------------------------------------
        {
            "entity"    : "PROD",
            "desc"      : "Set new max update date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         NewUpdateDate       = SYSDATE
                    WHERE       EntityType = 'PROD'
            """
        },
        {
            "entity"    : "PROD",
            "desc"      : "Create Delta entries for new records",
            "query"     : """
                INSERT INTO Stage0_Delta(EntityType, EntityId, FlagUpdated, FlagMain,
                                        FlagPrice, FlagComments, FlagRelated, LastUpdate)
                SELECT          'PROD'                  AS EntityType,
                                Id_Articulo             AS EntityId,
                                1                       AS FlagUpdated,
                                0                       AS FlagMain,
                                0                       AS FlagPrice,
                                0                       AS FlagComments,
                                0                       AS FlagRelated,
                                (SELECT     LastUpdateDate
                                    FROM    Stage0_DeltaControl
                                    WHERE   EntityType = 'PROD')
                                                        AS LastUpdate
                    FROM        Articulos
                    WHERE       Id_Articulo NOT IN (
                                    SELECT      EntityId
                                        FROM    Stage0_Delta
                                        WHERE   EntityType = 'PROD'
                                )
                    ORDER BY    Id_Articulo
            """
        },
        {
            "entity"    : "PROD",
            "desc"      : "Mark updated records",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'PROD')
                    WHERE       EntityType = 'PROD' AND
                                EntityId IN (
                                    --
                                    -- Articulos (NO INDEX ON F_Modi)
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD')
                                    UNION
                                    --
                                    -- Articulos_Textos (NO INDEX ON F_Modi)
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos_Textos A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD')
                                    UNION
                                    --
                                    -- Articulos_Auditorio (NO INDEX ON F_Modi)
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos_Auditorio A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD')
                                    UNION
                                    --
                                    -- Articulos_ISBN (NO INDEX ON F_Modi)
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos_ISBN A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD')
                                    UNION
                                    --
                                    -- Articulos_Autores (NO INDEX ON F_Modi)
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos_Autores A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD')
                                    UNION
                                    --
                                    -- Articulos_Autores_Biografia (NO INDEX ON F_Modi)
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos_Autores_Biografia A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD')
                                    UNION
                                    --
                                    -- Articulos_Temas_Musicales (NO INDEX ON F_Modi)
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos_Temas_Musicales A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD')
                                    UNION
                                    --
                                    -- Temas_Mus_Autores
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Temas_Mus_Autores A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD')
                                    UNION
                                    --
                                    -- Comentario_Articulos
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Comentario_Articulos A
                                        WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    A.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD')
                                    UNION
                                    --
                                    -- Tipos_Articulos
                                    --
                                    -- NOTE: this is indirect for changes on Tipos_Articulos
                                    --       and then the Id_Articulo for those Tipos_Articulos
                                    --
                                    SELECT          A.Id_Articulo
                                        FROM        Articulos A
                                        WHERE       A.Id_Tipo_Articulo IN (
                                                        SELECT      TA.Id_Tipo_Articulo
                                                            FROM    Tipos_Articulos TA
                                                            WHERE   TA.F_Modi >= (SELECT    DC.LastUpdateDate
                                                                                    FROM    Stage0_DeltaControl DC
                                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                                    TA.F_Modi <  (SELECT    DC.NewUpdateDate
                                                                                    FROM    Stage0_DeltaControl DC
                                                                                    WHERE   DC.EntityType = 'PROD')
                                                    )
                                )
            """ 
            ####
            #### NOTE: this subquery is not included because the RCO_Articulos_Relacionados
            ####       seems to not have F_Modi set in any record and it's an 80M records
            ####       table
            ####
            ####    /*
            ####     * THIS IS DONE WITH A TRIGGER BECAUSE
            ####     * THE TABLE RCO_Articulos_Relacionados
            ####     * DOES NOT HAVE AN INDEX ON F_MODI
            ####     *
            ####                        UNION
            ####                        --
            ####                        -- RCO_Articulos_Relacionados
            ####                        --
            ####                        SELECT          A.Id_Articulo
            ####                            FROM        RCO_Articulos_Relacionados A
            ####                            WHERE       A.F_Modi >= (SELECT     DC.LastUpdateDate
            ####                                                        FROM    Stage0_DeltaControl DC
            ####                                                        WHERE   DC.EntityType = 'PROD') AND
            ####                                        A.F_Modi <  (SELECT     DC.NewUpdateDate
            ####                                                        FROM    Stage0_DeltaControl DC
            ####                                                        WHERE   DC.EntityType = 'PROD')
            ####    */
        },
        #
        # TODO - check press notes
        # TODO - check interviews
        # TODO - check chapters
        #
        {
            "entity"    : "PROD",
            "desc"      : "Mark dependents - PAGE",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'PAGE')
                    WHERE       EntityType = 'PAGE' AND
                                EntityId = 1 AND
                                EXISTS (SELECT      1
                                            FROM    Stage0_Delta D
                                            WHERE   D.EntityType = 'PROD' AND
                                                    D.FlagUpdated = 1)
            """
        },
        {
            "entity"    : "PROD",
            "desc"      : "Set new last processed date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         LastUpdateDate      = NewUpdateDate
                    WHERE       EntityType = 'PROD'
            """
        },
        # ---------------------------------------------
        # ---------------------------------------------
        # --
        # -- entity PAGE
        # --
        # ---------------------------------------------
        # ---------------------------------------------
        {
            "entity"    : "PAGE",
            "desc"      : "Set new max update date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         NewUpdateDate       = SYSDATE
                    WHERE       EntityType = 'PAGE'
            """
        },
        {
            "entity"    : "PAGE",
            "desc"      : "Mark DIRECT updated records",
            "query"     : """
                UPDATE Stage0_Delta
                    SET         FlagUpdated         = 1,
                                LastUpdate          = 
                                        (SELECT     LastUpdateDate
                                            FROM    Stage0_DeltaControl
                                            WHERE   EntityType = 'PAGE')
                    WHERE       EntityType = 'PAGE' AND
                                EntityId = 1 AND
                                EXISTS (SELECT      1
                                            FROM    Articulos_Mesa_Recomendados M
                                            WHERE   M.En_Filtro = 'UTM' AND
                                                    M.Se_Muestra = 1 AND
                                                    M.F_Modi >= (SELECT     DC.LastUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD') AND
                                                    M.F_Modi <  (SELECT     DC.NewUpdateDate
                                                                    FROM    Stage0_DeltaControl DC
                                                                    WHERE   DC.EntityType = 'PROD'))
            """
        },
        # no dependents
        {
            "entity"    : "PAGE",
            "desc"      : "Set new last processed date",
            "query"     : """
                UPDATE Stage0_DeltaControl
                    SET         LastUpdateDate      = NewUpdateDate
                    WHERE       EntityType = 'PAGE'
            """
        }
    ]

    logger.info("Calculating updated records")
    print "Calculating updated records"
    print ""

    # iterate each step
    failed = False
    for s in range(len(queries)):

        # get handy data
        entity = queries[s]["entity"]
        desc   = queries[s]["desc"]
        query  = queries[s]["query"]

        print "Executing: %s %-45s " % (entity, desc),

        try:

            # get a connection and cursor
            conn = ecommerce.db.getConnection()
            cursor = conn.cursor()

            # execute the query
            cursor.execute(query)

            # commit changes
            conn.commit()

            print "OK"
            logger.info("OK - step %d - %s - %s" % (s, entity, desc))
        except:
            # rollback changes
            conn.rollback()

            print "ERROR"
            logger.error("ERROR - step %d - %s - %s" % (s, entity, desc))
            failed = True

    print ""

    # if failed => say something
    if failed:
        print "There were errors during the update"
        logger.error("ERROR - Calculating updated records")
    else:
        logger.info("OK - Calculated updated records")

    return -1 if failed else 0

