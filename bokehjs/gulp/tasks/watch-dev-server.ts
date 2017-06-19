import * as gulp from "gulp"
import * as runSequence from "run-sequence"
import * as paths from "../paths"
import * as child from 'child_process';

let node: any;

let serverRestart = () => {
  if (node) node.kill();
  node = child.spawn('node', ['devserver.js'], {stdio: 'inherit'});
  node.on('close', (code: number) => {
    if (code === 8) {
      console.log('Error detected, waiting for changes...');
    } else {
      console.log('Restarted server');
    }
  });
};

gulp.task("watch-dev-server", () => {

  serverRestart();

  gulp.watch(`${paths.coffee.watchSources}`, () => {
    runSequence("scripts:build", serverRestart)
  });

  gulp.watch(`${paths.less.watchSources}`, () => {
    runSequence("styles:build", serverRestart)
  });
})
