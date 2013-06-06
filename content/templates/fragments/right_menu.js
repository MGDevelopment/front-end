/**
 * right_menu.js
 */

function correctHeights(div1, div2, div3, div4, div5, div6, div7, div8, div9,
        div0) {
    var ddequalcolumns = new Object();
    ddequalcolumns.columnswatch = [ div1, div2, div3, div4, div5, div6, div7,
            div8, div9, div0 ];
    ddequalcolumns.setHeights = function(reset) {
        var tallest = 0;
        var resetit = (typeof reset == "string") ? true : false;
        for ( var i = 0; i < this.columnswatch.length; i++) {
            if (document.getElementById(this.columnswatch[i]) != null) {
                if (resetit) {
                    document.getElementById(this.columnswatch[i]).style.height = "auto";
                }
                if (document.getElementById(this.columnswatch[i]).offsetHeight > tallest) {
                    tallest = document.getElementById(this.columnswatch[i]).offsetHeight;
                }
            }
        }
        if (tallest > 0) {
            for ( var i = 0; i < this.columnswatch.length; i++) {
                if (document.getElementById(this.columnswatch[i]) != null) {
                    if (document.getElementById(this.columnswatch[i]).offsetHeight < tallest) {
                        document.getElementById(this.columnswatch[i]).style.height = tallest
                                + "px";
                    }
                }
            }
        }
    }
    ddequalcolumns.resetHeights = function() {
        this.setHeights("reset");
    }
    ddequalcolumns.dotask = function(target, functionref, tasktype) {
        var tasktype = (window.addEventListener) ? tasktype : "on" + tasktype;
        if (target.addEventListener) {
            target.addEventListener(tasktype, functionref, false);
        } else {
            if (target.attachEvent) {
                target.attachEvent(tasktype, functionref);
            }
        }
    }
    ddequalcolumns.dotask(window, function() {
        ddequalcolumns.setHeights();
    }, "load");
};
correctHeights("panelSeccSucursales", "panelSeccQuid", "seccionTematika",
        "panelSeccExtra", "panelSeccMusica", "panelSeccLibros",
        "panelSeccPeliculas", "panelSeccPasatiempos", "", "");