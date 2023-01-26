#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CdkPipelineStack } from '../lib/cdk_pipeline-stack';

const app = new cdk.App();
new CdkPipelineStack(app, 'CdkPipelineStack', {
  env: { account: process.env.ID, region: process.env.REGION },
});