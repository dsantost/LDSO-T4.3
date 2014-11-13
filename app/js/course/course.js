'use strict'
var inst= angular.module('inst',[]);

inst.filter('unsafe', function($sce) {
    return function(val) {
        return $sce.trustAsHtml(val);
    };
});

inst.controller('BgCtrl', function() {
  this.course = courseVar;
  this.subjects = subjectsVar;

});

inst.controller('histCtrl',function(){
  this.hist=historyVar;
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

var courseVar = {
        name: 'Universidade do Porto',
        local: 'Porto, Portugal',
        bgImg:'url(img/universities/up.jpg)',
        sidebarTitle:'Universidade do Porto',
        presSub:'Com origens que remontam ao século XVIII, a Universidade do Porto é uma das maiores instituições de ensino e investigação científica de Portugal e uma das 100 melhores universidades da Europa.',
        presText:'Mais de 31.000 estudantes, 2.300 professores e investigadores e 1.600 funcionários não docentes frequentam as suas 15 escolas e 60 unidades de investigação, distribuídas por três polos universitários localizados na cidade do Porto.<br />Com 14 faculdades e uma business school, a Universidade do Porto oferece uma excecional variedade de cursos, que abrangem todos os níveis de ensino superior e todas as grandes áreas do conhecimento. Na verdade, com mais de 600 programas de formação (das licenciaturas aos doutoramentos, passando pela educação contínua), a Universidade do Porto possui soluções de ensino para todos os públicos.<br />A qualificação de excelência do corpo docente (81% dos 1.608,2 docentes e investigadores ETI são doutorados) garante a elevada qualidade da formação da Universidade do Porto, que a torna na universidade portuguesa mais procurada pelos candidatos ao Ensino Superior e a preferida dos estudantes com as mais altas classificações escolares.<br />Todos os anos, cerca de 3.700 estudantes estrangeiros, de 146 diferentes países do mundo, frequentam a Universidade do Porto. E se 1.810 destes estudantes chegam através de programas internacionais de mobilidade, mais de metade deles (1.890) escolheram a U.Porto para realizar a totalidade do seu curso superior.<br />A Universidade do Porto é o maior produtor de Ciência em Portugal, sendo responsável por mais de 23% dos artigos científicos portugueses indexados anualmente na ISI Web of Science.<br />De facto, alguns dos mais produtivos e internacionalmente reconhecidos centros portugueses de Investigação e Desenvolvimento pertencem à Universidade do Porto. Mais de metade das suas 60 unidades de investigação foram classificadas com “Excelente” ou “Muito Bom” nas mais recentes avaliações independentes internacionais.<br />Nos últimos anos, a U.Porto tem apostado na valorização económica das suas atividades de investigação através de parcerias com algumas das maiores empresas nacionais que já resultaram em diversas inovações com sucesso comprovado em mercados nacionais e internacionais.<br />A inovação produzida pela Universidade também já conduziu à criação de mais de 120 patentes nacionais e internacionais e outras tantas empresas. Só no UPTEC - Parque de Ciência e Tecnologia da Universidade do Porto estão incubadas mais de uma centena de startups, responsáveis pela criação de 900 novos postos de trabalho qualificados.<br />Por tudo isto, a Universidade do Porto é a instituição portuguesa com a melhor classificação nos mais importantes rankings internacionais de Ensino e Investigação Científica, que sistematicamente colocam a U.Porto entre as 350 melhores universidades do mundo.'
};

var subjectsVar = [
  {
    sigla:'FAUP',
    nome:'Faculdade de Arquitectura da Universidade do Porto',
    img:'img/UP/FAUP.jpg'
  },
  {
    sigla:'FBAUP',
    nome:'Faculdade de Belas-Artes da Universidade do Porto',
    img:'img/UP/FBAUP.png'
  },{
    sigla:'FCUP',
    nome:'Faculdade de Ciências da Universidade do Porto',
    img:'img/UP/FCUP.jpg'
  },{
    sigla:'FCNAUP',
    nome:'Faculdade de Ciências da Nutrição e Alimentação da Universidade do Porto',
    img:'img/UP/FCNAUP.jpg'
  },{
    sigla:'FADEUP',
    nome:'Faculdade de Desporto da Universidade do Porto',
    img:'img/UP/FADEUP.jpg'
  },{
    sigla:'FDUP',
    nome:'Faculdade de Direito da Universidade do Porto',
    img:'img/UP/FDUP.jpg'
  },{
    sigla:'FEP',
    nome:'Faculdade de Economia da Universidade do Porto',
    img:'img/UP/FEP.jpg'
  },{
    sigla:'FEUP',
    nome:'Faculdade de Engenharia da Universidade do Porto',
    img:'img/UP/FEUP.jpg'
  },{
    sigla:'FFUP',
    nome:'Faculdade de Farmácia da Universidade do Porto',
    img:'img/UP/ICBAS_FFUP.jpg'
  },{
    sigla:'Faculdade de Letras da Universidade do Porto',
    nome:'FLUP',
    img:'img/UP/FLUP.jpg'
  },{
    sigla:'FMUP',
    nome:'Faculdade de Medicina da Universidade do Porto',
    img:'img/UP/FMUP.jpg'
  },{
    sigla:'FMDUP',
    nome:'Faculdade de Medicina Dentária da Universidade do Porto',
    img:'img/UP/FMDUP.jpg'
  },{
    sigla:'FPCEUP',
    nome:'Faculdade de Psicologia e de Ciências da Educação da Universidade do Porto',
    img:'img/UP/FPCEUP.jpg'
  },{
    sigla:'img/UP/ICBAS_FFUP.jpg',
    nome:'ICBAS',
    img:'Instituto de Ciências Biomédicas Abel Salazar'
  },]