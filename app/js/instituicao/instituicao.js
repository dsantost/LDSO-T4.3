'use strict'
var inst= angular.module('inst',[]);

inst.controller('BgCtrl', function() {
  this.institution = institutionVar;
});

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

var institutionVar = [{
        name: 'Universidade do Porto',
        local: 'Porto, Portugal',
        bgImg:'url(img/universities/up.jpg)'
}];
