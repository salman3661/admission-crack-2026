import React from 'react';
import { DecksView } from './DecksView';

export const HomeView: React.FC<React.ComponentProps<typeof DecksView>> = (props) => {
  return <DecksView {...props} />;
};

export default HomeView;
export { DecksView };
