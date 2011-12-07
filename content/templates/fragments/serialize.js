/**
 * serialize.js
 */

/**
* Implements JSON stringify and parse functions
* v1.0
*
* By Craig Buckler, Optimalworks.net
*
* Usage:
*
* // serialize a JavaScript object to a JSON string
* var str = JSON.stringify(object);
*
* // de-serialize a JSON string to a JavaScript object
* var obj = JSON.parse(str);
*/

var JSON = JSON || {};

//implement JSON.stringify serialization
JSON.stringify = JSON.stringify || function (obj) {

	var t = typeof (obj);
	if (t != "object" || obj === null) {

		// simple data type
		if (t == "string") obj = '"'+obj+'"';
		return String(obj);

	}
	else {

		// recurse array or object
		var n, v, json = [], arr = (obj && obj.constructor == Array);

		for (n in obj) {
			v = obj[n]; t = typeof(v);

			if (t == "string") v = '"'+v+'"';
			else if (t == "object" && v !== null) v = JSON.stringify(v);

			json.push((arr ? "" : '"' + n + '":') + String(v));
		}

		return (arr ? "[" : "{") + String(json) + (arr ? "]" : "}");
	}
};


//implement JSON.parse de-serialization
JSON.parse = JSON.parse || function (str) {
	if (str === "") str = '""';
	eval("var p=" + str + ";");
	return p;
};

function _serialize(obj) {
	//return JFather.serialize(obj);
	return JSON.stringify(obj);
}

function _unserialize(obj) {
	//return JFather.unserialize(obj);
	return JSON.parse(obj);
}