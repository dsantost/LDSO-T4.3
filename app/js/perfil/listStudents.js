'use strict'
var listStudents= angular.module('listStudents',[]);

listStudents.filter('unsafe', function($sce) {
    return function(val) {
        return $sce.trustAsHtml(val);
    };
});

var type='';

var studentsVar = [];

listStudents.controller('MainCtrl', function($scope, $http) {
 $http.get("http://uni-x.me/api/students/").success(
   function(response)
    {
        studentsVar = response;
        $scope.students = studentsVar;
    });
});