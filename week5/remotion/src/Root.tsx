import React from 'react';
import {Composition} from 'remotion';
import {LectureVideo} from './LectureVideo';

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="CGEnergy"
      component={LectureVideo}
      durationInFrames={3600}
      fps={30}
      width={1280}
      height={720}
    />
  );
};
