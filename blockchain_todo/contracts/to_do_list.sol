// SPDX-License-Identifier: GPL-3.0
//todo_list = await to_do_list.deployed()
pragma solidity >=0.5.0;

contract to_do_list {
    uint public task_count = 0;

    struct Task {
        uint id;
        string content;
        bool completed;
    }

    mapping(uint => Task) public tasks;
    
    constructor() public {
        create_task("do laundry");
    }

    function create_task(string memory _content) public {
        task_count ++;
        tasks[task_count] = Task(task_count, _content, false);
    }

}