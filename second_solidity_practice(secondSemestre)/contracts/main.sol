// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;


contract MyEstate {
    enum titeOfEstate {
        house,
        flat,
        loft
    }

    enum status {
        opened,
        closed
    }

    struct Estate {
        uint size;
        string estateAddress;
        address owner;
        titeOfEstate esType;
        bool status;
        uint idEstate;
    }

    
    struct Advertisement {
        address owner;
        address buyer;
        uint price;
        uint idEstate;
        uint dateTime;
        status adStatus;
    }

    Estate[] estate;
    Advertisement[] ads;

    mapping(address => uint) public balances;

    event adCreated();
    event estateCreated();
    event estateStatusChanged();
    event adStatusChanged();
    event estatePurchased();
    event fundsBack();

    modifier enoughValue(uint value, uint price){
        require(value >= price, "not have neough money");
        _;
    }

    modifier onlyEstateOwner(uint idEstate){
        require(estate[idEstate].owner == msg.sender, "you must be a estate owner");
        _;
    }

    modifier onlyAdOwner(uint idAd){
        require(ads[idAd].owner == msg.sender, "you must be a advertisement owner");
        _;
    }

    modifier isActiveEstate(uint idEstate){
        require(estate[idEstate].status, "this estate is not allow");
        _;
    }

    modifier isClosedAd(uint idAd){
        require(ads[idAd].adStatus == status.closed, "advertisement must be open");
        _;
    }

    modifier isEstateExist(uint idEstate){
        require(idEstate < 0 || idEstate >= estate.length, "estate isnt exist");
        _;
    }

    modifier isAdExist(uint idAd){
        require(idAd < 0 || idAd >= ads.length, "advertisement isnt exist");
        _;
    }

    function cretaeEstate(uint size, string memory estateAddress, titeOfEstate estype) public {
        require(size > 1, "size should be bigger 1");
        estate.push(Estate(size, estateAddress, msg.sender, estype, true, estate.length + 1));
        emit estateCreated();
    }

    function createAd() public {}

    function changeStatusEstate() public {}

    function chabgeStatusAd() public {}

    function withDraw() public {}

    function buyEstate() public {}

    function getBalance() public view returns(uint){}

    function getEstate() public view returns(Estate[] memory){
        return estate;
    }

    function getAds() public view returns(Advertisement[] memory){
        return ads;
    }
}