
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
        $scope.heading = 'Bem vindo ao Portal Académico';
        $scope.message = 'Encontre tudo o que quer saber sobre o Ensino Superior em Portugal!';
});

portal.controller('faqCtrl', function($scope) {
        $scope.heading = 'FAQ';
        $scope.message = 'Em construção';
});

portal.controller('contactCtrl', function($scope) {
        $scope.heading = 'Contatos';
        $scope.message = 'Em construção';
});

portal.controller('TabController', function(){
    this.tab = 1;

    this.setTab = function(newValue){
      this.tab = newValue;
    };

    this.isSet = function(tabName){
      return this.tab === tabName;
    }
});

portal.controller('VertNavCtrl', function($scope){
  var tabClasses;
  
  function initTabs() {
    tabClasses = ["","","",""];
  }
  
  $scope.getTabClass = function (tabNum) {
    return tabClasses[tabNum];
  };
  
  $scope.getTabPaneClass = function (tabNum) {
    return "tab-pane " + tabClasses[tabNum];
  }
  
  $scope.setActiveTab = function (tabNum) {
    initTabs();
    tabClasses[tabNum] = "active";
  };
  
  $scope.tab1 = "This is first section";
  $scope.tab2 = "This is SECOND section";
  $scope.tab3 = "This is THIRD section";
  $scope.tab4 = "This is FOUTRH section";
  
  //Initialize 
  initTabs();
  $scope.setActiveTab(1);
});