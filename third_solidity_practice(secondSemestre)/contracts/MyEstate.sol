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

    mapping(address=>uint) private  balances;

    modifier onlyEstateOwner(uint idEstate) {
        require(estate[idEstate].owner == msg.sender, "you must be a estate owner");
        _;
    }

    modifier onlyAdOwner(uint idAd) {
        require(ads[idAd].owner == msg.sender, "you must be a advertisement owner");
        _;
    }

    modifier isActiveEstate(uint idEstate) {
        require(estate[idEstate].status, "this estate is not allow");
        _;
    }

    modifier isClosedAd(uint idAd) {
        require(ads[idAd].adStatus == status.opened, "advertisement must be open");
        _;
    }

    modifier isEstateExist(uint idEstate) {
        require(idEstate >= 0 || idEstate <= estate.length, "estate isnt exist");
        _;
    }

    modifier isAdExist(uint idAd) {
        require(idAd >= 0 || idAd <= ads.length, "advertisement isnt exist");
        _;
    }

    event estateCreated(address _owner, uint _idAstate, uint _dateTime, titeOfEstate _esType);

    function cretaeEstate(uint size, string memory estateAddress, titeOfEstate estype) public {
        require(size > 1, "size should be bigger 1");
        estate.push(Estate(size, estateAddress, msg.sender, estype, true, estate.length + 1));
        emit estateCreated(msg.sender, estate.length + 1, block.timestamp, estype);
    }

    event adCreated(address _owner, uint _idEstate, uint _idAd, uint _dateTime, uint _price);

    function createAd(uint price, uint idEstate) public onlyEstateOwner(idEstate) isEstateExist(idEstate) isActiveEstate(idEstate) {
        ads.push(Advertisement(msg.sender, address(0), price, idEstate, block.timestamp, status.opened));
        emit adCreated(msg.sender, idEstate, ads.length + 1, block.timestamp, price);
    }

    event adStatusChanged(address _owner, uint _idEstate, uint idAd, uint _dateTime, status _adStatus);
    event estateStatusChanged(address _owner, uint _idEstate, uint _dateTime, bool _isActive);

    function changeStatusEstate(uint idEstate) public onlyEstateOwner(idEstate) isEstateExist(idEstate) {
        estate[idEstate].status = false;
        emit estateStatusChanged(msg.sender, idEstate, block.timestamp, false);

        for (uint i = 0; i < ads.length; i++) {
            if (ads[i].idEstate == idEstate) {
                ads[i].adStatus = status.closed;
                emit adStatusChanged(msg.sender, idEstate, i+1, block.timestamp, status.closed);
            }
        }
    }

    function changeStatusAd(uint adId) public onlyAdOwner(adId) isActiveEstate(ads[adId].idEstate) isAdExist(adId){
        ads[adId].adStatus == status.closed;
        emit adStatusChanged(msg.sender, ads[adId].idEstate, adId, block.timestamp, status.closed);
    }

    event fundsBack(address _to, uint _value, uint _dateTime);

    function withDraw(uint value) public {
        require(balances[msg.sender] >= value, "value must be less than or equal to balance");
        payable(msg.sender).transfer(value);
        balances[msg.sender] -= value;
        emit fundsBack(msg.sender, value, block.timestamp);
    }

    event estatePurchased(address _owner, address _buyer, uint _idAd, uint _idEstate, status _adStatus, uint _dateTime, uint _price);

    function buyEstate(uint adId) isClosedAd(adId) isAdExist(adId) public {
        require(balances[msg.sender] >= ads[adId].price, "not have enough money");
        require(msg.sender != ads[adId].owner, "You musnt be a owner");
        balances[msg.sender] -= ads[adId].price;
        balances[ads[adId].owner] += ads[adId].price;
        ads[adId].adStatus = status.closed;
        estate[ads[adId].idEstate].status = false;
        emit estatePurchased(ads[adId].owner, msg.sender, adId, ads[adId].idEstate, ads[adId].adStatus, block.timestamp, ads[adId].price);

    }

    function getBalance() public view returns(uint) {
        return balances[msg.sender];
    }

    function getEstates() public view returns(Estate[] memory) {
        return estate;
    }

    function getAds() public view returns(Advertisement[] memory) {
        return ads;
    }

    event Payd(address _from, uint _amount);

    function pay() public payable {
        balances[msg.sender] += msg.value;
        emit Payd(msg.sender, msg.value);
    }
}