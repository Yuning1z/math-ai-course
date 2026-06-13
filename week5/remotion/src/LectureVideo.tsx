import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  Audio,
} from 'remotion';

const points = [
  {x: 200, y: 520, label: 'x0'},
  {x: 420, y: 250, label: 'x1'},
  {x: 610, y: 390, label: 'x2'},
  {x: 760, y: 305, label: 'x3'},
  {x: 850, y: 330, label: 'x*'},
];

const SceneTitle: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      fontSize: 46,
      fontWeight: 700,
      color: '#102033',
      marginBottom: 20,
    }}
  >
    {children}
  </div>
);

const Formula: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      fontSize: 34,
      color: '#16324f',
      background: '#eef5ff',
      borderLeft: '8px solid #2f6fbb',
      padding: '18px 24px',
      borderRadius: 8,
      fontFamily: 'Georgia, serif',
    }}
  >
    {children}
  </div>
);

export const LectureVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const sceneDuration = 450;
  const scene = Math.floor(frame / sceneDuration);
  const local = frame % sceneDuration;
  const fade = interpolate(local, [0, 45, 395, 448], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Comment-driven generation cue:
  // Draw the quadratic energy as contour ellipses and animate CG iterates as
  // large corrective moves that do not undo earlier minimizations.
  const pathProgress = interpolate(frame, [830, 2920], [0, points.length - 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const activeIndex = Math.min(points.length - 1, Math.floor(pathProgress));
  const nextIndex = Math.min(points.length - 1, activeIndex + 1);
  const blend = pathProgress - activeIndex;
  const currentX =
    points[activeIndex].x * (1 - blend) + points[nextIndex].x * blend;
  const currentY =
    points[activeIndex].y * (1 - blend) + points[nextIndex].y * blend;

  const pulse = spring({frame, fps, config: {damping: 12, stiffness: 90}});

  return (
    <AbsoluteFill
      style={{
        background: 'linear-gradient(135deg, #f8fbff 0%, #f7f2e8 100%)',
        fontFamily: 'Inter, Arial, sans-serif',
      }}
    >
      <Audio src={staticFile('narration.mp3')} />
      <svg
        width="1280"
        height="720"
        viewBox="0 0 1280 720"
        style={{position: 'absolute', inset: 0}}
      >
        <g transform="translate(580 350) rotate(-22)">
          {[260, 210, 160, 110, 65].map((r, i) => (
            <ellipse
              key={r}
              cx="0"
              cy="0"
              rx={r * 1.45}
              ry={r * 0.62}
              fill="none"
              stroke={i === 4 ? '#2f6fbb' : '#9fb4c8'}
              strokeWidth={i === 4 ? 3 : 2}
              opacity={0.34 + i * 0.1}
            />
          ))}
        </g>
        <polyline
          points={points
            .slice(0, activeIndex + 1)
            .map((p) => `${p.x},${p.y}`)
            .join(' ')}
          fill="none"
          stroke="#b23a48"
          strokeWidth="5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <line
          x1={points[activeIndex].x}
          y1={points[activeIndex].y}
          x2={currentX}
          y2={currentY}
          stroke="#b23a48"
          strokeWidth="5"
          strokeLinecap="round"
        />
        {points.map((p, i) => (
          <g key={p.label}>
            <circle
              cx={p.x}
              cy={p.y}
              r={i <= activeIndex ? 10 : 6}
              fill={i === points.length - 1 ? '#1d7a55' : '#b23a48'}
              opacity={i <= activeIndex || i === points.length - 1 ? 1 : 0.35}
            />
            <text x={p.x + 12} y={p.y - 10} fontSize="22" fill="#102033">
              {p.label}
            </text>
          </g>
        ))}
        <circle
          cx={currentX}
          cy={currentY}
          r={12 + 4 * pulse}
          fill="#f2b134"
          stroke="#102033"
          strokeWidth="3"
        />
      </svg>

      <div
        style={{
          position: 'absolute',
          left: 70,
          top: 60,
          width: 500,
          opacity: fade,
        }}
      >
        {scene <= 0 && (
          <>
            <SceneTitle>Conjugate Gradient</SceneTitle>
            <Formula>CG = energy minimization over Krylov spaces</Formula>
          </>
        )}
        {scene === 1 && (
          <>
            <SceneTitle>Quadratic Energy</SceneTitle>
            <Formula>phi(x) = 1/2 x^T A x - b^T x</Formula>
          </>
        )}
        {scene === 2 && (
          <>
            <SceneTitle>Residual = Negative Gradient</SceneTitle>
            <Formula>r_k = b - A x_k = -grad phi(x_k)</Formula>
          </>
        )}
        {scene === 3 && (
          <>
            <SceneTitle>Why Zigzags Happen</SceneTitle>
            <Formula>Steepest descent forgets the energy geometry</Formula>
          </>
        )}
        {scene === 4 && (
          <>
            <SceneTitle>Conjugate Directions</SceneTitle>
            <Formula>p_i^T A p_j = 0 for i not equal j</Formula>
          </>
        )}
        {scene === 5 && (
          <>
            <SceneTitle>Krylov Optimality</SceneTitle>
            <Formula>x_k minimizes over x_0 + K_k(A, r_0)</Formula>
          </>
        )}
        {scene === 6 && (
          <>
            <SceneTitle>Convergence</SceneTitle>
            <Formula>spectral geometry controls speed</Formula>
          </>
        )}
        {scene >= 7 && (
          <>
            <SceneTitle>Takeaway</SceneTitle>
            <Formula>preconditioning improves the geometry before CG starts</Formula>
          </>
        )}
      </div>
    </AbsoluteFill>
  );
};
