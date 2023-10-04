// SPDX-License-Identifier: MIT
pragma solidity >=0.4.0 <0.9.0;

contract election{
    
    uint votes1; // BJP
    uint votes2; // TDP + JSP
    uint votes3; // YSCRP

    mapping (address=>bool) _voters;
    // mapping specific address to boolean data type

    function contestVote(uint contestant) public {
        require(!_voters[msg.sender]); // verifying that whether i've voted or not

        if(contestant==1){
            votes1+=1;
        } else if(contestant==2){
            votes2+=1;
        } else if(contestant==3){
            votes3+=1;
        }
        _voters[msg.sender]=true; 
        // i'm telling the blockchain that this user has been participated in polling
    }

    function viewVotes() public view returns(uint,uint,uint) {
        return (votes1,votes2,votes3);
    }
}

