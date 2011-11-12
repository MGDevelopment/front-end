/**
* home-showcase.js
*/
var dataShowCase = {};

{%- if showcase_data_TMK_RDAM -%}
dataShowCase['TMK_RDAMBooks'] = '{{ showcase_data_TMK_RDAM.books|replace("\n", "") }}';
dataShowCase['TMK_RDAMMusic'] = '{{ showcase_data_TMK_RDAM.music|replace("\n", "") }}';
dataShowCase['TMK_RDAMMovies'] = '{{ showcase_data_TMK_RDAM.movies|replace("\n", "") }}';
dataShowCase['TMK_RDAMGames'] = '{{ showcase_data_TMK_RDAM.games|replace("\n", "") }}';
{%- endif %}
{%- if showcase_data_TMK_RDAY -%}
dataShowCase['TMK_RDAYBooks'] = '{{ showcase_data_TMK_RDAY.books|replace("\n", "") }}';
dataShowCase['TMK_RDAYMusic'] = '{{ showcase_data_TMK_RDAY.music|replace("\n", "") }}';
dataShowCase['TMK_RDAYMovies'] = '{{ showcase_data_TMK_RDAY.movies|replace("\n", "") }}';
dataShowCase['TMK_RDAYGames'] = '{{ showcase_data_TMK_RDAY.games|replace("\n", "") }}';
{%- endif %}
{%- if showcase_data_TMK_RDAT -%}
dataShowCase['TMK_RDATBooks'] = '{{ showcase_data_TMK_RDAT.books|replace("\n", "") }}';
dataShowCase['TMK_RDATMusic'] = '{{ showcase_data_TMK_RDAT.music|replace("\n", "") }}';
dataShowCase['TMK_RDATMovies'] = '{{ showcase_data_TMK_RDAT.movies|replace("\n", "") }}';
dataShowCase['TMK_RDATGames'] = '{{ showcase_data_TMK_RDAT.games|replace("\n", "") }}';
{%- endif %}

{%- if showcase_data_MVM -%}
dataShowCase['MVMBooks'] = '{{ showcase_data_MVM.books|replace("\n", "") }}';
dataShowCase['MVMMusic'] = '{{ showcase_data_MVM.music|replace("\n", "") }}';
dataShowCase['MVMMovies'] = '{{ showcase_data_MVM.movies|replace("\n", "") }}';
dataShowCase['MVMGames'] = '{{ showcase_data_MVM.games|replace("\n", "") }}';
{%- endif %}
{%- if showcase_data_MVY -%}
dataShowCase['MVYBooks'] = '{{ showcase_data_MVY.books|replace("\n", "") }}';
dataShowCase['MVYMusic'] = '{{ showcase_data_MVY.music|replace("\n", "") }}';
dataShowCase['MVYMovies'] = '{{ showcase_data_MVY.movies|replace("\n", "") }}';
dataShowCase['MVYGames'] = '{{ showcase_data_MVY.games|replace("\n", "") }}';
{%- endif %}
{%- if showcase_data_MVT -%}
dataShowCase['MVTBooks'] = '{{ showcase_data_MVT.books|replace("\n", "") }}';
dataShowCase['MVTMusic'] = '{{ showcase_data_MVT.music|replace("\n", "") }}';
dataShowCase['MVTMovies'] = '{{ showcase_data_MVT.movies|replace("\n", "") }}';
dataShowCase['MVTGames'] = '{{ showcase_data_MVT.games|replace("\n", "") }}';
{%- endif %}

{%- if showcase_data_MPM -%}
dataShowCase['MPMBooks'] = '{{ showcase_data_MPM.books|replace("\n", "") }}';
dataShowCase['MPMMusic'] = '{{ showcase_data_MPM.music|replace("\n", "") }}';
dataShowCase['MPMMovies'] = '{{ showcase_data_MPM.movies|replace("\n", "") }}';
dataShowCase['MPMGames'] = '{{ showcase_data_MPM.games|replace("\n", "") }}';
{%- endif %}
{%- if showcase_data_MPY -%}
dataShowCase['MPYBooks'] = '{{ showcase_data_MPY.books|replace("\n", "") }}';
dataShowCase['MPYMusic'] = '{{ showcase_data_MPY.music|replace("\n", "") }}';
dataShowCase['MPYMovies'] = '{{ showcase_data_MPY.movies|replace("\n", "") }}';
dataShowCase['MPYGames'] = '{{ showcase_data_MPY.games|replace("\n", "") }}';
{%- endif %}
{%- if showcase_data_MPT -%}
dataShowCase['MPTBooks'] = '{{ showcase_data_MPT.books|replace("\n", "") }}';
dataShowCase['MPTMusic'] = '{{ showcase_data_MPT.music|replace("\n", "") }}';
dataShowCase['MPTMovies'] = '{{ showcase_data_MPT.movies|replace("\n", "") }}';
dataShowCase['MPTGames'] = '{{ showcase_data_MPT.games|replace("\n", "") }}';
{%- endif %}

{%- if showcase_data_MVAM -%}
dataShowCase['MVAMBooks'] = '{{ showcase_data_MVAM.books|replace("\n", "") }}';
dataShowCase['MVAMMusic'] = '{{ showcase_data_MVAM.music|replace("\n", "") }}';
dataShowCase['MVAMMovies'] = '{{ showcase_data_MVAM.movies|replace("\n", "") }}';
dataShowCase['MVAMGames'] = '{{ showcase_data_MVAM.games|replace("\n", "") }}';
{%- endif %}
{%- if showcase_data_MVAY -%}
dataShowCase['MVAYBooks'] = '{{ showcase_data_MVAY.books|replace("\n", "") }}';
dataShowCase['MVAYMusic'] = '{{ showcase_data_MVAY.music|replace("\n", "") }}';
dataShowCase['MVAYMovies'] = '{{ showcase_data_MVAY.movies|replace("\n", "") }}';
dataShowCase['MVAYGames'] = '{{ showcase_data_MVAY.games|replace("\n", "") }}';
{%- endif %}
{%- if showcase_data_MVAT -%}
dataShowCase['MVATBooks'] = '{{ showcase_data_MVAT.books|replace("\n", "") }}';
dataShowCase['MVATMusic'] = '{{ showcase_data_MVAT.music|replace("\n", "") }}';
dataShowCase['MVATMovies'] = '{{ showcase_data_MVAT.movies|replace("\n", "") }}';
dataShowCase['MVATGames'] = '{{ showcase_data_MVAT.games|replace("\n", "") }}';
{%- endif %}

function loadShowCase() {
	TMK.addData('showcase', dataShowCase);
	return;
} 

var callBackDropDownShowCase = function (section) {
	
	return;
}
loadShowCase();

