
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