angular.module('catms.services', []).
service('taskAPIservice', function($http) {
  this.getTasks = function() {
    console.log('hello')
    return $http({
      method: 'GET',
      url: '/api/v1/tasks'
    });
  }
});
