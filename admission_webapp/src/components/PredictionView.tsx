import React from 'react';
import { PredictorView } from './PredictorView';

export const PredictionView: React.FC<React.ComponentProps<typeof PredictorView>> = (props) => {
  return <PredictorView {...props} />;
};

export default PredictionView;
export { PredictorView };
