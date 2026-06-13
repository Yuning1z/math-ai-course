import {readFileSync, mkdirSync} from 'node:fs';
import {resolve} from 'node:path';
import {spawnSync} from 'node:child_process';

const projectRoot = resolve(import.meta.dirname, '..');
const courseRoot = resolve(projectRoot, '..');
const narrationPath = resolve(courseRoot, 'narration-script.md');
const publicDir = resolve(projectRoot, 'public');
const mediaPath = resolve(publicDir, 'narration.mp3');
const subtitlePath = resolve(publicDir, 'narration.vtt');

const markdown = readFileSync(narrationPath, 'utf8');
const narration = markdown
  .split('\n')
  .filter((line) => !line.startsWith('#'))
  .join('\n')
  .replace(/\$([^$]+)\$/g, '$1')
  .replace(/\\mathcal\{K\}/g, 'Krylov K')
  .replace(/\\phi/g, 'phi')
  .replace(/\s+/g, ' ')
  .trim();

mkdirSync(publicDir, {recursive: true});

const result = spawnSync(
  'edge-tts',
  [
    '--voice',
    'en-US-JennyNeural',
    '--text',
    narration,
    '--write-media',
    mediaPath,
    '--write-subtitles',
    subtitlePath,
  ],
  {stdio: 'inherit'}
);

if (result.error?.code === 'ENOENT') {
  console.error(
    'edge-tts is not installed. Install it with: pip install edge-tts'
  );
  process.exit(1);
}

process.exit(result.status ?? 1);
