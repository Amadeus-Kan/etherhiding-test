//SPDX-License-Identifier:MIT
pragma solidity ^0.8.19;

contract urlstorage{
    string public storedUrl;
    constructor(string memory _initialUrl){
        storedUrl = _initialUrl;
    }
    function updateUrl(string memory _newUrl) public {
        storedUrl = _newUrl;
    }
}