const code2 = `function square(n) {
  return n * n;
}`;
let ast2 = require("@babel/parser").parse(code2)
console.log(ast2)
console.log('-------------------分割线-------------------------------')
console.log(ast2['program']['body'])
console.log('-------------------分割线-------------------------------')
const fs = require('fs');
const {parse} = require("@babel/parser");

const traverse = require("@babel/traverse").default;
//引入模块
const generator = require("@babel/generator").default;

const code = `function square(n) {
  return n * n;
}`;

const ast = parse(code);

traverse(ast, {
    enter(path) {
        if (path.isIdentifier({ name: "n" })) {
            path.node.name = "x";
        }
    }
});
// AST --> 代码
const output = generator(ast)["code"]
console.log(output)
console.log(output['body'])