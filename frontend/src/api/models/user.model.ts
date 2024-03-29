import { BloodRequest, DonationRequest } from ".";

export namespace UserDto {
  export interface Item {
    id: number;
    email: string;
    contact_group: {
      hidden: boolean;
      phone: string;
      email: string;
    };
    first_name: string;
    middle_name: string;
    last_name: string;
    city: null | string;
    vkid: null | string;
    wishes: string;
    available_weekends_only: boolean;
    avaliable_time: [string, string][];
    avatar?: string;
    requests: BloodRequest[];
    donations: DonationRequest[];
  }

  export interface Update {
    email: string;
    first_name: string;
    middle_name: string;
    last_name: string;
    city: string;
    wishes: string;
    available_weekends_only: boolean;
    avaliable_time: [string, string][];
    contact_group: {
      hidden: boolean;
      phone: string;
      email: string;
    };
  }
}
