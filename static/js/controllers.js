angular.module('catms.controllers', []).
controller('mainController', function($scope, taskAPIservice) {
  $scope.taskList = [];
  taskAPIservice.getTasks().then(function (response) {
      //Dig into the responde to get the relevant data
      console.log(response)
      $scope.taskList = response.data.taskList;
  });
});
