
var uniX= angular.module('uniX', ['ngRoute']);


uniX.config(function($routeProvider) {

$routeProvider
        // route for the home page
        .when('/', {
            redirectTo : '../index.html'
                //controller  : 'mainCtrl'
        })

        // route for the FAQ page
        .when('/universidades', {
            redirectTo : '../universidades.html'
        //controller  : 'faqCtrl'
        })

        // route for the contact page
        .when('/cursos', {
            redirectTo : '../course.html'
                //controller  : 'contactCtrl'
        })

        .when('/estudantes',{
            redirectTo : '../estudantes.html'
        })
        ;
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