'use strict'
var listCour= angular.module('listCour',[]);


listCour.filter('unsafe', function($sce) {
    return function(val) {
        return $sce.trustAsHtml(val);
    };
});

var type='';

var coursesVar = [];

listCour.controller('MainCtrl', function($http) {
 $http.get("http://localhost:8000/api/degrees/").success(
   function(response)
    {
        for(var i=0; i<response.length; i++)
        {
            console.log(response);
            coursesVar.push(response[i]);
            /*if (response[i].category=="Universidade")
            {
                universitiesVar.push(response[i]);
            }*/
        }
    });
    this.courses = coursesVar;

});