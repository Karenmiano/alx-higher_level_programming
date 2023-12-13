#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let i = 0;
    for (let elem of list) {
        if (elem === searchElement) {
            i++;
        }
    }
    return (i);
};