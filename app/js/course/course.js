'use strict'
var cour = angular.module('cour',[]);

cour.filter('unsafe', function($sce) {
    return function(val) {
        return $sce.trustAsHtml(val);
    };
});

var type='';

/* Variables
var courseVar = {
        name: '',
        local: '',
        bgImg:'',
        sidebarTitle:'',
        presSub:'',
        presText:'',
        saidasText:'',
        viasText:''
};

var provasVar = {
};


var studentsVar = {
  heading:'',
  subheading:'',
  content:[]
};
  
var commentVar=[];
  
*/

/* CONTROLLERS


inst.controller('MainCtrl', function($http) {
 $http.get("http://localhost:8000/api/degrees").success(
   function(response)
    {
      courseVar.name=response.name;
      courseVar.local=response.address;
      courseVar.bgImg='';//response.name;
      courseVar.sidebarTitle=response.name;
      courseVar.presSub=response.presentation_heading;
      courseVar.presText=response.presentation;
      courseVar.saidasText=response.saidas;
      courseVar.viasText=response.vias;
      studentsVar.heading=response.students_heading;
      stundentsVar.content=response.students;
      commentVar=response.comments;
      type=response.category;
    });

});
*/

cour.controller('BgCtrl', function($http) {
    $http.get("http://localhost:8001/api/degrees/1/").success(
   function(response)
    {
    //  console.log(response);
      $scope.institution=response;
    });
  this.course = courseVar;
  this.subjects = subjectsVar;
    this.provas = provasVar;

});



cour.controller('histCtrl',function(){
  this.hist=historyVar;
});

cour.controller('studentCtrl',function(){
  this.students=students;
});

cour.controller('initMap',function(){
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
        bgImg:'url(img/institutions/up.jpg)',
        sidebarTitle:'Universidade do Porto',
        presSub:'O ensino da Engenharia Informática e Computação foi concebido na FEUP como requerendo um ciclo de formação e aprendizagem completo de cinco anos integrados, correspondendo aos 1º e 2º ciclos da implementação do Processo de Bolonha e conferindo de imediato o grau de Mestre.',
        presText:'O MIEIC pretende então alcançar, entre outros objetivos, as seguintes metas:<li>Proporcionar formação científica e de engenharia de base sólida, fundamental para a interação com outras especialidades da Engenharia e como suporte a uma prática profissional de excelência;<li>Proporcionar formação profissional sólida e especializada que permita a conceção, especificação, projeto e realização de produtos, processos e serviços, tendo como base os Computadores, a Computação e as Tecnologias da Informação;<li>Fomentar a aquisição de competências não-técnicas, como o desenvolvimento das capacidades e atitudes criativa, crítica, trabalho em equipa e liderança; fomentar a aquisição do espírito empreendedor e de iniciativa, avaliação de riscos e aproveitamento de oportunidades;<li>Proporcionar formação que vise o desenvolvimento e prática de processos de gestão em engenharia com objetivos, entre outros, de incentivar um bom aproveitamento de meios e o aumento da qualidade e produtividade;<li>Fornecer a formação necessária para a atribuição do título profissional de Engenheiro, a conferir pela Ordem dos Engenheiros. <br> <br>No final dos três primeiros anos (1º ciclo) do MIEIC os alunos estarão providos de uma sólida formação de base, abrangendo as competências científicas e de engenharia essenciais, mas também os conhecimentos fundamentais de banda larga nas diversas áreas da informática, embora sem qualquer especialização. Este primeiro degrau é visto sobretudo como possibilitador de mobilidade de e para outras escolas nacionais e europeias. No final dos cinco anos do curso os diplomados terão uma formação avançada em Engenharia Informática e Computação, podendo ter escolhido uma área de especialização ou manter um leque mais alargado de interesses, mercê de uma ampla oferta de opções, configurável individualmente, contida no plano de estudos. As possíveis especializações incluem atualmente:Engenharia de Software e Sistemas de Informação (2 sub-áreas com estes nomes), Redes e Tecnologias de Informação (sub-áreas de Tecnologias da Internet e de Infra-estruturas Informáticas), Sistemas Inteligentes e Multimédia (2 sub-áreas com estes nomes)',
        saidasText: 'Entre as múltiplas possibilidades de funções profissionais dos diplomados pelo MIEIC destacam-se as seguintes:<li>Arquitetura e conceção de sistemas de informação;<li>Gestão de sistemas informáticos ou de centros de informática;<li>Conceção e desenvolvimento de sistemas e aplicações;<li>Gestão de projectos informáticos;<li>Consultadoria e auditoria;<li>Investigação ou desenvolvimento tecnológico.<br><br><br>Nos empregadores típicos para os Engenheiros Informáticos da FEUP incluem-se os seguintes:<li>Empresas de desenvolvimento de software;<li>Empresas fornecedoras de serviços informáticos;<li>Empresas de serviços como a banca e seguros;<li>Empresas que integrem os seus próprios centros de serviços informáticos em áreas tais como os transportes, a distribuição, a logística, etc.;<li>Instituições de investigação e desenvolvimento.',
        viasText: '<li><h5> Alunos sem Licenciatura</h5><br>Ingressam no 1º ano. Após os três primeiros anos podem obter o grau de Licenciado em Ciências da Engenharia - orientação em Engenharia Informática e Computação. No final dos cinco anos do MIEIC será concedido o grau de Mestre<br><br><li><h5>Alunos Licenciados</h5><br>Ingressam no 4º ano com alguma possível variação dependendo do grau de afinidade e da profundidade dos estudos superiores já efetuados. A duração dos estudos no MIEIC poderá ir de 1 a 5 semestres, sendo normalmente de 4 semestres para Licenciados de três anos em Engenharia Informática. No final será concedido o grau de Mestre</li></ul>',
};

var provasVar=
    {
        prova1: 'Física e Química',
        prova2: 'Matemática',
        prova3: 'Matemática',
        prova4: 'Português',
        minimCand: "100 pontos",
        minimIngre: "95 pontos"
    };

var subjectsVar = [
  {
    codigo:'EIC0011',
    sigla:'MDIS',
    nome:'Matemática Discreta',
    creditos:'6'
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

    
var students = {
  heading:'Os nossos alunos',
  subheading:'Nos quais depositamos o nosso futuro.',
  content:[
    {
      image:'img/students/3.jpg',
      name:'Daniel Teixeira',
      mail:'ei10067@fe.up.pt'
    },
    {
      image:'img/students/2.jpg',
      name:'Diogo Ribeiro',
      mail:'ei11005@fe.up.pt'
    },
    {
      image:'img/students/1.jpg',
      name:'Hugo Cardoso',
      mail:'ei11154@fe.up.pt'
    },
    {
      image:'img/students/4.jpg',
      name:'João Monteiro',
      mail:'ei11055@fe.up.pt'
    },
    {
      image:'img/students/5.jpg',
      name:'Vasco Gomes',
      mail:'ei11161@fe.up.pt'
    },
  ]
};