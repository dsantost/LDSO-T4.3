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
        presSub:'O ensino da Engenharia Informática e Computação foi concebido na FEUP como requerendo um ciclo de formação e aprendizagem completo de cinco anos integrados, correspondendo aos 1º e 2º ciclos da implementação do Processo de Bolonha e conferindo de imediato o grau de Mestre.',
        presText:'O MIEIC pretende então alcançar, entre outros objetivos, as seguintes metas:<br><br> - Proporcionar formação científica e de engenharia de base sólida, fundamental para a interação com outras especialidades da Engenharia e como suporte a uma prática profissional de excelência;<br> - Proporcionar formação profissional sólida e especializada que permita a conceção, especificação, projeto e realização de produtos, processos e serviços, tendo como base os Computadores, a Computação e as Tecnologias da Informação;<br> - Fomentar a aquisição de competências não-técnicas, como o desenvolvimento das capacidades e atitudes criativa, crítica, trabalho em equipa e liderança; fomentar a aquisição do espírito empreendedor e de iniciativa, avaliação de riscos e aproveitamento de oportunidades;<br> - Proporcionar formação que vise o desenvolvimento e prática de processos de gestão em engenharia com objetivos, entre outros, de incentivar um bom aproveitamento de meios e o aumento da qualidade e produtividade;<br> - Fornecer a formação necessária para a atribuição do título profissional de Engenheiro, a conferir pela Ordem dos Engenheiros. <br> <br>No final dos três primeiros anos (1º ciclo) do MIEIC os alunos estarão providos de uma sólida formação de base, abrangendo as competências científicas e de engenharia essenciais, mas também os conhecimentos fundamentais de banda larga nas diversas áreas da informática, embora sem qualquer especialização. Este primeiro degrau é visto sobretudo como possibilitador de mobilidade de e para outras escolas nacionais e europeias. No final dos cinco anos do curso os diplomados terão uma formação avançada em Engenharia Informática e Computação, podendo ter escolhido uma área de especialização ou manter um leque mais alargado de interesses, mercê de uma ampla oferta de opções, configurável individualmente, contida no plano de estudos. As possíveis especializações incluem atualmente:Engenharia de Software e Sistemas de Informação (2 sub-áreas com estes nomes), Redes e Tecnologias de Informação (sub-áreas de Tecnologias da Internet e de Infra-estruturas Informáticas), Sistemas Inteligentes e Multimédia (2 sub-áreas com estes nomes)'
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