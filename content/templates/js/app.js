/**
 * closure principal 
 */

APP = (function() {
    var data = {};
    return {
        addData: function(name, value) {
            data[name] = value;
        },
        getData: function(name) {
            return data[name];
        }
    }
})();
