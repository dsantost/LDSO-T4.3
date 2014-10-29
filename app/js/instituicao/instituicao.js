(function(){
var inst= angular.module('inst', ['ngRoute']);

 inst.controller('bgCtrl', function() {
    this.institution = institutionVar;

  });

inst.config(function($routeProvider) {
 
$routeProvider
   /*     // route for the home page
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
        });*/
});


/*
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

portal.controller('TabController', function(){
    this.tab = 1;

    this.setTab = function(newValue){
      this.tab = newValue;
    };

    this.isSet = function(tabName){
      return this.tab === tabName;
    }
});*/

inst.controller('initMap',function(){
    var mapProp = {
      center:new google.maps.LatLng(41.146661, -8.615571),
      zoom:15,
      mapTypeId:google.maps.MapTypeId.ROADMAP
      };
    var map=new google.maps.Map(document.getElementById("googleMap")
      ,mapProp);
    google.maps.event.addDomListener(window, 'load', initialize);
});

inst.controller('bg',function()){

});

var institutionVar = [{
        name: "Universidade do Porto",
        local: "Porto, Portugal",
        bgImage:'url(img/universities/up.jpg)'

}];

})();