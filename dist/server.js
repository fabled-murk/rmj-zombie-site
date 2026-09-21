// Minimal static file server. Listens on $PORT (required by the platform).
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const PORT = process.env.PORT || 8080;
const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.json': 'application/json; charset=utf-8',
};

http
  .createServer((req, res) => {
    let rel = decodeURIComponent(req.url.split('?')[0]);
    if (rel.endsWith('/')) rel += 'index.html';
    const file = path.normalize(path.join(ROOT, rel));
    if (!file.startsWith(ROOT)) {
      res.writeHead(403).end('forbidden');
      return;
    }
    fs.readFile(file, (err, buf) => {
      if (err) {
        fs.readFile(path.join(ROOT, 'index.html'), (e2, fallback) => {
          if (e2) return res.writeHead(404).end('not found');
          res.writeHead(200, { 'content-type': TYPES['.html'] }).end(fallback);
        });
        return;
      }
      const type = TYPES[path.extname(file).toLowerCase()] || 'application/octet-stream';
      const cache = /\.(jpg|jpeg|png|svg)$/i.test(file) ? 'public, max-age=86400' : 'no-cache';
      res.writeHead(200, { 'content-type': type, 'cache-control': cache }).end(buf);
    });
  })
  .listen(PORT, () => console.log(`zombie-site listening on ${PORT}`));
