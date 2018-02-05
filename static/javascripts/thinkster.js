(function () {
    'use strict';

    angular
        .module('thinkster', [
            'thinkster.config',
            'thinkster.routes',
            'thinkster.authentication'
        ]);

    angular
        .module('thinkster.routes', ['ngRoute']);

    angular
        .module('thinkster.config', []);
})();

angular
    .module('thinkster')
    .run(run);

run.$inject = ['$http'];

function run($http) {
    $http.defaults.xsrfHeaderName = 'x-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
}