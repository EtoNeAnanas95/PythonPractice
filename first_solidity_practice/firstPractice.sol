// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;


contract Practice1 {

    mapping (address => uint) private users;

    constructor() {
        users[msg.sender] = 0;
    }

    event Paid(address _from, uint _amount);

    struct Person { //не нужная штука, потому я использовал маппинг
        address userAddress;
        uint256 balance;
    }

    function getBalance(address _address) public view returns(uint) {
        return users[_address];
    }

    function pay() public payable {
        emit Paid(msg.sender, msg.value);
        users[msg.sender] += msg.value;
    }

    function withdrawall(address payable _to, uint _amount) public {
        require(_to != address(0), "to must be not zero address");
        require(_amount > 0, "amount must be > 0");
        require(_amount < users[msg.sender], "you cannot transfer more money than your balance");
        _to.transfer(_amount * 1000000000000000000);

        users[msg.sender] -= _amount;
        users[_to] = _amount;
    }
}