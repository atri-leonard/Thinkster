(function () {
    'use strict';

    angular
        .module('thinkster.authentication.service') //Register in module
        .factory('Authentication', Authentication); //Register into module

    Authentication.$inject = ['$cookies', '$http']; //We inject these as dependencies to our module

    function Authentication($cookies, $http) {
        var Authentication = {
            register: register
        };
        return Authentication;
        function register(email, password, username) {
            return $http.post('/api/v1/accounts/', {
                username: username,
                password: password,
                email: email
            });
        }
    }
})();