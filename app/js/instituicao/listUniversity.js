'use strict'
var listUni= angular.module('listUni',[]);


listUni.filter('unsafe', function($sce) {
    return function(val) {
        return $sce.trustAsHtml(val);
    };
});

var type='';

var universitiesVar = [];

listUni.controller('MainCtrl', function($http) {
 $http.get("http://localhost:8000/api/institutions/").success(
   function(response)
    {
        for(var i=0; i<response.length; i++)
        {
            universitiesVar.push(response[i]);
            /*if (response[i].category=="Universidade")
            {
                universitiesVar.push(response[i]);
            }*/
        }
    });
    this.universities = universitiesVar;

});