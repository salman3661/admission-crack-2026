import React from 'react';
import 'katex/dist/katex.min.css';
import { InlineMath, BlockMath } from 'react-katex';
import { VaultView } from './VaultView';
import { MathText } from './MathText';

export const ShortcutVaultView: React.FC<React.ComponentProps<typeof VaultView>> = (props) => {
  return <VaultView {...props} />;
};

export default ShortcutVaultView;
export { VaultView, MathText, InlineMath, BlockMath };
