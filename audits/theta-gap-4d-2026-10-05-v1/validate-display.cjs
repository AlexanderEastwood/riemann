// Display-logic validation only. No theta values, sign scan or proof certificate.
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const html = fs.readFileSync(path.join(__dirname,'theta-gap-4d-2026-10-05-v1.html'),'utf8');
const source = html.match(/<script>([\s\S]*?)<\/script>/)[1];
const boundCode = source.match(/const bound = (.*);/)[1];
const expressionCode = source.match(/const expression = (.*);/)[1];
const bound = Function('return ('+boundCode+');')();
const expression = Function('return ('+expressionCode+');')();
const close = (a,b) => assert.ok(Math.abs(a-b)<=1e-12*(1+Math.abs(a)+Math.abs(b)),`${a} != ${b}`);
// Independent product differentiation of X=pY/4, including zero and negative Y.
const cases = [[0,.5,0,-1],[.5,.5,.5,.5],[.5,.5,.5,-.5],
  [.5,.5,.1,.5],[.5,0,.5,.5],[1,-.75,.5,-.4],[2,1,-.2,1],[0,0,0,2]];
for(const [r,y,v,w] of cases){
  const p=r*r+.25, X=p*y/4, Xp=(2*r*y+p*v)/4, Xpp=(2*y+4*r*v+p*w)/4;
  close(expression(r,y,v,w),16*(Xp*Xp-X*Xpp));
  if(y!==0){
    const b=bound(r,y,v);close(expression(r,y,v,b),0);
    assert.ok(expression(r,y,v,b-Math.sign(y)*.25)>0);
    assert.ok(expression(r,y,v,b+Math.sign(y)*.25)<0);
  }
}
assert.equal(expression(.5,.5,.5,.5),0);
assert.ok(expression(.5,.5,.5,-.5)>0);
assert.ok(expression(.5,.5,.1,.5)<0);
close(expression(.5,0,.5,.5),.0625);
assert.equal(expression(0,0,0,-2),0);
assert.equal(expression(2,0,0,2),0);
assert.ok(!/<style|stylesheet|<script\s+src/i.test(html));
assert.ok(html.includes('prefers-reduced-motion'));
assert.ok(html.includes('No zeta values or original theta trajectory'));
assert.ok(html.includes('That inequality alone would not prove RH.'));
console.log(JSON.stringify({kind:'display validation, not arithmetic research',
  product_identity_examples:cases.length,sign_direction_and_zero_cases:'passed',
  source_style_and_scope_checks:'passed'}));
