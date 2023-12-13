#!/usr/bin/node

exports.converter = function (base) {
    const thebase = base;
    function result (num) {
        return num.toString(base);
    }
    return result;
};