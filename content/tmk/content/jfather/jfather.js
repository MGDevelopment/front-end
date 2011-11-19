/*
	Copyright (c) 2010 Max Power
	
	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:
	
	The above copyright notice and this permission notice shall be included in
	all copies or substantial portions of the Software.
	
	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
	THE SOFTWARE.
	
*/
	
	/*****************************************************************
	 *  Script:         jfather.js                                   *
	 *  Description:    Functions to serialize/unserialize objects   *
	 *  Author:         Max Power                                    *
	 *  Version:        1.0                                          *
	 *  Date:           10/09/2010                                   *
	 *****************************************************************/
	
	/**
	 *	Class:			JFather
	 *	Description:	Serialize/Unserialize objects
	 **/
	
	function JFather() {
	}
	
	/**
	 *	Constants
	 **/
	
	JFather.TYPE_NUMBER    = 'number';
	JFather.TYPE_BOOLEAN   = 'boolean';
	JFather.TYPE_STRING    = 'string';
	JFather.TYPE_FUNCTION  = 'function';
	JFather.TYPE_OBJECT    = 'object';
	JFather.TYPE_UNDEFINED = 'undefined';
	
	JFather.FIELD_NAME  = 'name';
	JFather.FIELD_VALUE = 'value';
	JFather.FIELD_CLASS = 'class';
	JFather.FIELD_ARGS  = 'args';
	JFather.FIELD_BODY  = 'body';
	
	JFather.EMPTY    = '';
	JFather.SPACE    = ' ';
	JFather.STA_DECL = '(';
	JFather.END_DECL = ')';
	JFather.ARGS_SEP = ',';
	JFather.TRUE_VAL = 'true';
	JFather.RET_NEW  = 'return new ';
	
	/**
	 *	Return the class name of the object
	 **/
	
	JFather.getClassName = function(obj) {
		return (obj == null) ? JFather.EMPTY : obj.__proto__.constructor.name;
	}
	
	/**
	 *	Return a xml string of the serialized object
	 **/
	
	JFather.serialize = function(obj) {
		var xml = document.implementation.createDocument(JFather.EMPTY, JFather.EMPTY, null);
		JFather.marshall(JFather.EMPTY, obj, xml, xml);
		
		return (new XMLSerializer()).serializeToString(xml);
	}
	
	/**
	 *	Append a new child with the serialized object
	 **/
	
	JFather.marshall = function(name, obj, xml, node) {
		var type = typeof(obj);
		
		if ((type != JFather.TYPE_UNDEFINED) && (type != JFather.TYPE_FUNCTION)) {
			
			var current = xml.createElement(type);
			current.setAttribute(JFather.FIELD_NAME, name);
			
			if ((type == JFather.TYPE_NUMBER) || (type == JFather.TYPE_BOOLEAN) || (type == JFather.TYPE_STRING))
				current.setAttribute(JFather.FIELD_VALUE, escape(obj));
			else if (type == JFather.TYPE_OBJECT) {
				current.setAttribute(JFather.FIELD_CLASS, JFather.getClassName(obj));
				
				for (field in obj)
					JFather.marshall(field, obj[field], xml, current);
			}
			
			node.appendChild(current);
		}
	}
	
	/**
	 *	Return the object unserialized
	 **/
	
	JFather.unserialize = function(text) {
		return JFather.unmarshall(((new DOMParser()).parseFromString(text, 'text/xml')).documentElement);
	}
	
	/**
	 *	Return the object unserialized
	 **/
	
	JFather.unmarshall = function(node) {
		var result = null;
		
		if (node.nodeName == JFather.TYPE_NUMBER)
			result = parseFloat(unescape(node.getAttribute(JFather.FIELD_VALUE)));
		else if (node.nodeName == JFather.TYPE_BOOLEAN)
			result = unescape(node.getAttribute(JFather.FIELD_VALUE)) == JFather.TRUE_VAL;
		else if (node.nodeName == JFather.TYPE_STRING)
			result = unescape(node.getAttribute(JFather.FIELD_VALUE));
		else if (node.nodeName == JFather.TYPE_OBJECT) {
			if (node.getAttribute(JFather.FIELD_CLASS) != JFather.EMPTY) {
				var classFunction = new Function(JFather.EMPTY, JFather.RET_NEW + node.getAttribute(JFather.FIELD_CLASS) + JFather.STA_DECL + JFather.END_DECL);
				result = classFunction();
				
				for (var index = 0; index < node.childNodes.length; index++)
					result[node.childNodes[index].getAttribute(JFather.FIELD_NAME)] = JFather.unmarshall(node.childNodes[index]);
			}
		}
		
		return result;
	}