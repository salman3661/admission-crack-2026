import React from 'react';
import { VaultView } from './VaultView';

export const ShortcutVaultView: React.FC<React.ComponentProps<typeof VaultView>> = (props) => {
  return <VaultView {...props} />;
};

export default ShortcutVaultView;
export { VaultView };
