'use strict'
var profile= angular.module('profile',[]);

profile.filter('unsafe', function($sce) {
    return function(val) {
        return $sce.trustAsHtml(val);
    };
});

profile.controller('BackgroundCtrl', function() {
  this.student = studentVar;
  this.interests = interestsVar;
});

var studentVar = {
        name: 'João Monteiro',
        local: 'Porto, Portugal',
        bgImg:'url(img/banner.jpg)',
        birthdate: '9 de Maio de 1993',
        civilstatus: 'Solteiro',
        institution:'Faculdade de Engenharia da Universidade do Porto',
        institutionabb:'FEUP'
        course:'Mestrado Integrado em Engenharia Informática e Computação',
        courseabb:'MIEIC'
};

var interestsVar = [
	{
		Bem-estar animal
	},
	{
		Arte e Cultura
	},
	{
		Ação social
	},
	{
		Educação
	},
	{
		Ambiente
	},
	{
		Direitos humanos
	},
]