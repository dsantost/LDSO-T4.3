'use strict'
var uniX= angular.module('uniX', ['ngRoute','inst']);


uniX.config(function($routeProvider) {

$routeProvider
        .when('/home', {
            templateUrl : 'home.html'
        })

        .when('/universidades', {
            templateUrl : 'university.html',
        })

        .when('/cursos', {
            templateUrl : 'course.html'
        })

        .when('/estudantes',{
            templateUrl : 'profile.html'
        })
        ;
});


uniX.controller('UnivCtrl',function(){
    //uniX=inst;
});
// create the controller and inject Angular's $scope
/*
uniX.controller('mainCtrl', function($scope) {
        // create a message to display in our view
        $scope.heading = 'Welcome to Portal Académico';
        $scope.message = 'Here you will find the meaning of life.';
});

uniX.controller('faqCtrl', function($scope) {
        $scope.heading = 'FAQ';
        $scope.message = 'This is where you will find the accumulated knowledge of the world.';
});

uniX.controller('contactCtrl', function($scope) {
        $scope.heading = 'Contact us';
        $scope.message = 'Contact us';
});

uniX.controller('TabController', function(){
    this.tab = 1;

    this.setTab = function(newValue){
      this.tab = newValue;
    };

    this.isSet = function(tabName){
      return this.tab === tabName;
    }
});*/