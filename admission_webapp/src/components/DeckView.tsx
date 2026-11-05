import React from 'react';
import { DecksView } from './DecksView';

export const DeckView: React.FC<React.ComponentProps<typeof DecksView>> = (props) => {
  return <DecksView {...props} />;
};

export default DeckView;
export { DecksView };
