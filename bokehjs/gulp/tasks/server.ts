import * as gulp from "gulp";
import * as child from 'child_process';

let node: any;

gulp.task('server', () => {
  if (node) node.kill();
  node = child.spawn('node', ['devserver.js'], {stdio: 'inherit'});
  node.on('close', (code: number) => {
    if (code === 8) {
      console.log('Error detected, waiting for changes...');
    }
  });
})
