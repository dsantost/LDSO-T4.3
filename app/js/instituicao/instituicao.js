'use strict'
var inst= angular.module('inst',[]);


inst.filter('unsafe', function($sce) {
    return function(val) {
        return $sce.trustAsHtml(val);
    };
});
/*
inst.controller('serviceController',['Institution',  function (Institution) {
   // console.log("Institution.controller");
    this.serviceVar = Institution.query();
}]);*/


/*function customersController($scope,$http) {
    $http.get("http://www.w3schools.com/website/Customers_JSON.php")
    .success(function(response) {$scope.names = response;});
}
*//*
inst.controller('BgCtrl', function($http) {
  //this.institution = institutionVar;
 this.institution=function() {
 $http.get("http://localhost:8001/api/institutions/1/").success(
   function(response)
    {
    //  console.log(response);
      return response;
    });
}
this.faculties = facultiesVar;

});*/

inst.controller('BgCtrl', function($http,$scope) {
  //this.institution = institutionVar;
 $http.get("http://localhost:8000/api/institutions/1/").success(
   function(response)
    {
    //  console.log(response);
      $scope.institution=response;
    });
this.institution=institutionVar;
this.faculties = facultiesVar;

});

inst.controller('histCtrl',function(){
  this.hist=historyVar;
});

inst.controller('studentCtrl',function(){
  this.students=students;
});

inst.controller('commentCtrl',function(){
  this.comment=commentVar;
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

var institutionVar = {
        name: 'Universidade do Porto',
        local: 'Porto, Portugal',
        bgImg:'url(img/universities/up.jpg)',
        sidebarTitle:'Universidade do Porto',
        presSub:'Com origens que remontam ao século XVIII, a Universidade do Porto é uma das maiores instituições de ensino e investigação científica de Portugal e uma das 100 melhores universidades da Europa.',
        presText:'Mais de 31.000 estudantes, 2.300 professores e investigadores e 1.600 funcionários não docentes frequentam as suas 15 escolas e 60 unidades de investigação, distribuídas por três polos universitários localizados na cidade do Porto.<br />Com 14 faculdades e uma business school, a Universidade do Porto oferece uma excecional variedade de cursos, que abrangem todos os níveis de ensino superior e todas as grandes áreas do conhecimento. Na verdade, com mais de 600 programas de formação (das licenciaturas aos doutoramentos, passando pela educação contínua), a Universidade do Porto possui soluções de ensino para todos os públicos.<br />A qualificação de excelência do corpo docente (81% dos 1.608,2 docentes e investigadores ETI são doutorados) garante a elevada qualidade da formação da Universidade do Porto, que a torna na universidade portuguesa mais procurada pelos candidatos ao Ensino Superior e a preferida dos estudantes com as mais altas classificações escolares.<br />Todos os anos, cerca de 3.700 estudantes estrangeiros, de 146 diferentes países do mundo, frequentam a Universidade do Porto. E se 1.810 destes estudantes chegam através de programas internacionais de mobilidade, mais de metade deles (1.890) escolheram a U.Porto para realizar a totalidade do seu curso superior.<br />A Universidade do Porto é o maior produtor de Ciência em Portugal, sendo responsável por mais de 23% dos artigos científicos portugueses indexados anualmente na ISI Web of Science.<br />De facto, alguns dos mais produtivos e internacionalmente reconhecidos centros portugueses de Investigação e Desenvolvimento pertencem à Universidade do Porto. Mais de metade das suas 60 unidades de investigação foram classificadas com “Excelente” ou “Muito Bom” nas mais recentes avaliações independentes internacionais.<br />Nos últimos anos, a U.Porto tem apostado na valorização económica das suas atividades de investigação através de parcerias com algumas das maiores empresas nacionais que já resultaram em diversas inovações com sucesso comprovado em mercados nacionais e internacionais.<br />A inovação produzida pela Universidade também já conduziu à criação de mais de 120 patentes nacionais e internacionais e outras tantas empresas. Só no UPTEC - Parque de Ciência e Tecnologia da Universidade do Porto estão incubadas mais de uma centena de startups, responsáveis pela criação de 900 novos postos de trabalho qualificados.<br />Por tudo isto, a Universidade do Porto é a instituição portuguesa com a melhor classificação nos mais importantes rankings internacionais de Ensino e Investigação Científica, que sistematicamente colocam a U.Porto entre as 350 melhores universidades do mundo.'
};

var historyVar = {
  subTitle: 'Há mais de um século a criar profissionais de excelência.',
  content:[
    {
      image:'img/UP/1.jpg',
      heading:'Março 1911',
      subheading:'Fundação da Universidade',
      contentText:'A Universidade do Porto foi fundada por decreto de 22 de Março de 1911, emanado do Governo Provisório da República. Se bem que seja possível apontar como as suas antecessoras mais remotas a Aula de Náutica, estabelecida por D. José I em 1762, e a Aula de Debuxo e Desenho, criada por D. Maria I em 1779, a Universidade vai basear-se fundamentalmente sobre instituições de ensino superior criadas no século XIX: a Academia Politécnica e a Escola Médico-Cirúrgica do Porto.'
    },
    {
      image:'img/UP/2.jpg',
      heading:'Abril 1911',
      subheading:'Primeira grande reestruturação',
      contentText:'A implantação da República, em 5 de Outubro de 1910, provocou importantes modificações no campo do ensino, nomeadamente a criação de duas universidades, a de Lisboa e a do Porto. Pelo decreto de 19 de Abril de 1911, a Universidade do Porto ficou assim constituída: uma Faculdade de Ciências Matemáticas, Físico-Químicas e Histórico-Naturais, uma Faculdade de Medicina com uma Escola de Farmácia anexa e ainda uma Faculdade de Comércio que nunca se concretizou. A Faculdade de Ciências anexava uma Escola de Engenharia.'
    },
    {
      image:'img/UP/3.jpg',
      heading:'Julho 1911',
      subheading:'Inauguração',
      contentText:'A UP foi inaugurada a 16 de Julho de 1911 e, nesse mesmo dia, foi eleito o primeiro Reitor, o matemático Gomes Teixeira. A partir de agora é confiado à Universidade o seu próprio governo económico e científico. Também a autonomia do ensino é reconhecida. O governo da Universidade pertence aos corpos Académicos: Senado, Assembleia Geral dos Professores, Conselhos das Faculdades e Escolas e aos seus Delegados efectivos - Director e Reitor.'
    },
    {
      image:'img/UP/4.jpg',
      heading:'Abril 1974',
      subheading:'Expansão pós-revolução',
      contentText:'A Universidade do Porto conheceu uma grande expansão com a revolução de Abril de 1974. Às seis faculdades existentes juntaram-se, como criação de raiz ou escolas integradas, as seguintes: ICBAS - Instituto de Ciências Biomédicas Abel Salazar (1975), Faculdade de Ciências do Desporto e de Educação Física (1975), Faculdade de Psicologia e de Ciências da Educação (1977), Faculdade de Arquitectura (1979), Faculdade de Medicina Dentária (1989), Faculdade de Ciências da Nutrição e da Alimentação (1992), Faculdade de Belas Artes (1992) e Faculdade de Direito (1994).'
    },
  ],
  last:'Faz <br />história <br />connosco!'
};

var students = {
  heading:'Os nossos alunos',
  subheading:'Nos quais depositamos o nosso futuro.',
  content:[
    {
      image:'img/team/1.jpg',
      name:'Daniel Teixeira',
      mail:'ei10067@fe.up.pt'
    },
    {
      image:'img/team/2.jpg',
      name:'Diogo Ribeiro',
      mail:'ei11005@fe.up.pt'
    },
    {
      image:'img/team/3.jpg',
      name:'Hugo Cardoso',
      mail:'ei11154@fe.up.pt'
    },
    {
      image:'img/team/4.jpg',
      name:'João Monteiro',
      mail:'ei11055@fe.up.pt'
    },
    {
      image:'img/team/5.jpg',
      name:'Vasco Gomes',
      mail:'ei11161@fe.up.pt'
    },
  ]
};

var commentVar=[
  {
    image:'img/team/4.jpg',
    name:'João Monteiro',
    date:'4 de outubro de 2014, 10:49',
    comment:'Estou na UP desde 2011 e posso dizer que é uma unibersidade muito boa. Sou aluno da FEUP e a nossa é a melhor faculdade da melhor unibersidade do melhor país.',
    replies:[
      {
        image:'img/team/1.jpg',
        name:'Daniel Teixeira',
        date:'4 de outubro de 2014, 10:51',
        comment:'*universidade'
      },
    ]
  },
  {
    image:'img/team/2.jpg',
    name:'Diogo Ribeiro',
    date:'10 de outubro de 2014, 22:12',
    comment:'Se vais ser caloiro, manda-me MP. Posso-te responder ao que quiseres sobre a UP.',
    replies:[

    ]
  },
  {
    image:'img/team/3.jpg',
    name:'Hugo Cardoso',
    date:'13 de outubro de 2014, 02:14',
    comment:'UP FTW, FEUP FTW, ISEP FTL.',
    replies:[

    ]
  },
  {
    image:'img/team/5.jpg',
    name:'Vasco Gomes',
    date:'19 de outubro de 2014, 17:26',
    comment:'Estou no MIEIC na FEUP na UP em PT na UE.',
    replies:[

    ]
  },
];
var facultiesVar = [
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
