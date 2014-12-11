'use strict'
var profile= angular.module('profile',[]);


profile.filter('unsafe', function($sce) {
	return function(val) {
		return $sce.trustAsHtml(val);
	};
});

profile.controller('bgCtrl', function() {
	this.student=studentVar;
});

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