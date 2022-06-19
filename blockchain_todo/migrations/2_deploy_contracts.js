const to_do_list = artifacts.require("./to_do_list.sol");

module.exports = function(deployer) {
  deployer.deploy(to_do_list);
};
