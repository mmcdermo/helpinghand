/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

var server = "http://localhost:8000/";
var stack = [];

var app = {
    // Application Constructor
    initialize: function() {	
        this.bindEvents();
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicity call 'app.receivedEvent(...);'
    onDeviceReady: function() {
	//call server for main menu and ready the device
	stack.push("menu/main");
	app.callForContent("menu/main");
	app.receivedEvent('deviceready');
    },

    callForContent: function(query) {
	//check cache
	var data = window.localStorage.getItem(query);
/*	if (data !== null) { //cache hit
	    $("#deviceready").html(data);
	    $("a").on("touchend", app.clickItem);		
	}
	else {//cache miss: make a query to server*/
	    $.ajax({
		url: server+query,
	    }).done(function (result) {
		var content = $(result).find('div').html();//parse out the div with the content
		$("#deviceready").html(content);
		$("a").on("touchend", app.clickItem);
		window.localStorage.setItem(query,content);
	    });
	//}
	
	//re-register touch events
    },

    clickItem: function(event) {
	//an a tag was clicked, which amounts to a button.
	var id = event.target.id;
	if (id === "back") {
	    if (stack.length > 1) {
		stack.pop();
		app.callForContent(stack[stack.length-1]);
	    }
	}
	else {
	    id = id.replace(/\./,"/");
	    stack.push(id);
	    app.callForContent(id);
	}
    },

    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }
};

