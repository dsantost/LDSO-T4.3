var portal= angular.module('portal', ['ngRoute']);


portal.config(function($routeProvider) {

$routeProvider
        // route for the home page
        .when('/', {
                templateUrl : 'nav/home.html',
                controller  : 'mainCtrl'
        })

        // route for the FAQ page
        .when('/faq', {
        templateUrl : 'nav/faq.html',
        controller  : 'faqCtrl'
        })

        // route for the contact page
        .when('/contact', {
                templateUrl : 'nav/contact.html',
                controller  : 'contactCtrl'
        });
});

// create the controller and inject Angular's $scope
portal.controller('mainCtrl', function($scope) {
        // create a message to display in our view
        $scope.heading = 'Welcome to Portal Académico';
        $scope.message = 'Here you will find the meaning of life.';
});

portal.controller('faqCtrl', function($scope) {
        $scope.heading = 'FAQ';
        $scope.message = 'This is where you will find the accumulated knowledge of the world.';
});

portal.controller('contactCtrl', function($scope) {
        $scope.heading = 'Contact us';
        $scope.message = 'Contact us';
});