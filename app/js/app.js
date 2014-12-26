
var uniX= angular.module('uniX', []);

uniX.controller('loginController',function($scope,$http){
    $scope.login = function () {
        console.log("login");
    }
});

uniX.controller('registerController',function($scope,$http){
    $scope.email = '';
    $scope.username = '';
    $scope.password = '';
    $scope.name = '';
    $scope.register = function () { 
    $http({
       url:'http://localhost:8000/api/users/',
       method: 'POST',
       data:{username: this.username, email: this.email,password: this.password },
       })
       .success(function(response){
        $http({
            url:'http://localhost:8000/api/students/',
            method: 'POST',
            traditional:true,
            data:{id:response.id,user:response.id,name:$scope.name},
        }).success(function(){
           console.log("Registado com sucesso");
        }).error(function(response){
            console.log(response);
        });
       })
    .error(function(response){
        console.log(response);
    });
    }
     
});

uniX.controller('loginController',function($scope,$http,$window){
    $scope.user = {username:'',password:''};
    $scope.message = '';
    $scope.login = function () { 
    $http
    .post('/authenticate/',$scope.user)
    .success(function (data,status,headers,config){
      $window.sessionStorage.toke=data.token;
        $scope.message = 'Seja bem vindo';
    })
    .error(function (data,status,headers,config){
        delete $window.sessionStorage.token;
        $scope.message = 'Error: Invalid user of password';
    });
    }
     
});

uniX.factory('authInterceptor', function ($rootScope, $q, $window) {
  return {
    request: function (config) {
      config.headers = config.headers || {};
      if ($window.sessionStorage.token) {
        config.headers.Authorization = 'Bearer ' + $window.sessionStorage.token;
      }
      return config;
    },
    response: function (response) {
      if (response.status === 401) {
          
      }
      return response || $q.when(response);
    }
  };
});

uniX.config(function ($httpProvider) {
  $httpProvider.interceptors.push('authInterceptor');
});


