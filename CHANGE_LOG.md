
# v0.8.3
- Removed ABCI re-exports.  You must import the full proper module path
   `abci.application`
   `abci.server`
   `abci.utils`
   You can also access all the tendermint protobuf classes in the `tendermint` package
- Refactored to src directory
- Change readme to markdown
- More tests