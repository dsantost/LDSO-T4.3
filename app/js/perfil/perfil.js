'use strict'
var profile= angular.module('profile',[]);
var sd=
	{
		bgimage:'url(img/banner.jpg)',
		profilepic:'img/team/1.jpg'
	};

profile.filter('unsafe', function($sce) {
	return function(val) {
		return $sce.trustAsHtml(val);
	};
});

profile.controller('stCtrl', function($scope, $http) {
	$http.get('http://uni-x.me/api/students/1/').
		success(function(response) {
			$scope.student=response;
			$scope.staticdata=sd;

			$http.get('http://uni-x.me/api/institutions/').success(function(resp) {
				$scope.institutions=[];
				for(var i=0;i<$scope.student.enrollments.length;i++) {
					for(var j=0;j<resp.length;j++) {
						if (resp[j].id == $scope.student.enrollments[i].institution) {
							var inst = {
								name: '',
								abbr: '',
								year:'',
								active:''};
							inst.name = resp[j].name;
							inst.abbr = resp[j].abbr;
							inst.year = $scope.student.enrollments[i].year;
							inst.active = $scope.student.enrollments[i].active;
							$scope.institutions.push(inst);

						}
					}
				}
			});

			$http.get('http://uni-x.me/api/cities/').success(function(resp) {
				$scope.city="";
					for(var i=0;i<resp.length;i++) {
						if (resp[i].id == $scope.student.city) {
							$scope.city = resp[i].name;
						}
					}
			});
		});
});

profile.controller('skillsCtrl', function($http,$scope) {
	$http.get("http://uni-x.me/api/students/1/").success(
		function(response)
		{
			$scope.expert=[];
			$scope.proficient=[];
			$scope.intermediate=[];
			for(var i=0;i<response.skills.length;i++){
				if(response.skills[i].level == "Expert")
					$scope.expert.push(response.skills[i]);
				else if(response.skills[i].level == "Proficient")
					$scope.proficient.push(response.skills[i]);
				else if(response.skills[i].level == "Intermediate")
					$scope.intermediate.push(response.skills[i]);
			}
		});
});

profile.controller('langsCtrl', function($http,$scope) {
	$http.get("http://uni-x.me/api/students/1/").success(
		function(response)
		{
			$scope.fluent=[];
			$scope.basic=[];
			for(var i=0;i<response.languages.length;i++){
				if(response.languages[i].level == 1 || response.languages[i].level == 2)
					$scope.fluent.push(response.languages[i]);
				else if(response.languages[i].level == 3 || response.languages[i].level == 4)
					$scope.basic.push(response.languages[i]);
			}
		});
});

profile.controller('coursesCtrl', function($scope, $http) {
	$http.get('http://uni-x.me/api/degrees/').
		success(function(response) {
			$scope.degrees=response;
			$http.get('http://uni-x.me/api/institutions/').success(function(resp) {
				$scope.institutions=resp;
			});

		});
});

/*

profile.controller('volCtrl',function(){
	this.vol=volunteeringVar;
});

profile.controller('skillsCtrl',function(){
	this.skills=skillsVar;
});

profile.controller('certsCtrl',function(){
	this.certificates=certsVar;
});

profile.controller('langsCtrl',function(){
	this.languages=langsVar;
});

profile.controller('eduCtrl',function(){
	this.education=eduVar;
});

profile.controller('intsCtrl',function(){
	this.interests=intsVar;
});

profile.controller('portCtrl',function(){
	this.portfolio=portVar;
});

var studentVar = {
	name: 'João Monteiro',
	profilepic: 'img/team/4.jpg',
	local: 'Porto, Portugal',
	bgImg:'url(img/banner.jpg)',
	birthdate: '9 de Maio de 1993',
	civilstatus: 'Solteiro',
	institution:'Faculdade de Engenharia da Universidade do Porto',
	institutionabb:'FEUP',
	course:'Mestrado Integrado em Engenharia Informática e Computação',
	courseabb:'MIEIC'
};

var volunteeringVar = {
	interests:[
		{
			name: 'Bem-estar animal'
		},
		{
			name: 'Arte e Cultura'
		},
		{
			name: 'Ação social'
		},
		{
			name: 'Educação'
		},
		{
			name: 'Ambiente'
		},
		{
			name: 'Direitos humanos'
		},
	],
	done:[
		{
			name: 'Banco Alimentar'
		},
	]
};

var skillsVar = {
	best:[
		{
			name: 'C++'
		},
		{
			name: 'Java'
		},
		{
			name: 'HTML'
		},
	],
	moderate:[
		{
			name: 'Desenvolvimento ágil de software'
		},
		{
			name: 'AngularJS'
		},
	]
};

var certsVar = {
	list:[
		{
			name: 'Certificate of Proficiency in English',
			grade: 'A',
			entity: 'Universidade de Cambridge',
			vality: 'Ilimitada'
		},
	]
};

var langsVar = {
	fluent:[
		{
			name: 'Português'
		},
		{
			name: 'Inglês'
		},
	],
	basic:[
		{
			name: 'Francês'
		},
		{
			name: 'Espanhol'
		},
	]
};

var eduVar = {
	secondary:[
		{
			name: 'Escola Secundária Dr. Mário Sacramento',
			year: '12.º ano'
		},
	],
	superior:[
		{
			name: 'Faculdade de Engenharia da Universidade do Porto',
			degree: 'Mestrado Integrado em Engenharia Informática e Computação'
		},
	]
};


var intsVar = {
	list:[
		{
			name: 'Fotografia'
		},
		{
			name: 'Literatura'
		},
		{
			name: 'Cinematografia'
		},
	]
};

var portVar = {
	items: [
		{
			name: 'Jogo "Raiden"',
			degree: 'MIEIC',
			img: 'img/UP/mieic_p1.jpg'
		},
		{
			name: 'uni-X"',
			degree: 'MIEIC',
			img: 'img/UP/mieic_p2.jpg'
		},
		{
			name: 'Apresentação "Rosewood Hotels"',
			degree: 'MIEIC',
			img: 'img/UP/mieic_p3.jpg'
		},
	]
}

	*/