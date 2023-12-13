#!/usr/bin/node

exports.converter = function (base) {
    function result (num) {
        return num.toString(base);
    }
    return result;
};